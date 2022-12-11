import requests, config, jwt, markdown
from flask import Flask, abort, request, jsonify
from utils.youtube import get_channel_id_from_handle
from flask_cors import CORS
from tube2blog.worker import Worker
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

app = Flask(__name__)
CORS(app)

# add celery config
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"
celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)

# sqlalchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///streamline.db"
db.init_app(app)

from models import VideoQueue

with app.app_context():
    from models import *

    db.create_all()


@app.get("/api/verify_handle/<handle>")
def verify_channel(handle="@parttimelarry"):
    channel_id = get_channel_id_from_handle(handle)

    if channel_id is None:
        abort(500)

    return {"code": "success", "channel_id": channel_id}


@app.get("/api/fetch_channel_videos/<channel_id>")
def fetch_channel_videos(channel_id):
    page = request.args.get("page", 1)

    url = f"https://www.googleapis.com/youtube/v3/search?key={config.YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    r = requests.get(url)

    return r.json()


@app.post("/api/enqueue_videos")
def enqueue_videos():
    # accepts json post with video_ids
    data = request.json

    for video_id in data["video_ids"]:
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        video = VideoQueue()
        video.video_id = video_id
        video.status = "queued"
        video.queued_timestamp = datetime.now()
        db.session.add(video)
        db.session.commit()

        prepare_video_transcript.delay(video_url)

    return {"code": "success"}


@app.post("/api/update_video_status/<video_id>")
def update_video_status(video_id):
    data = request.json

    video = VideoQueue.query.filter(VideoQueue.video_id == video_id).first()
    if video is None:
        abort(500, "Video not found")

    video.status = data["status"]
    video.transcript = data["transcript"]
    video.markdown = data["markdown"]

    if data["status"] == "finished":
        video.finished_timestamp = datetime.now()

    # Admin API key goes here
    key = config.GHOST_ADMIN_API_KEY

    # Split the key into ID and SECRET
    id, secret = key.split(":")

    # Prepare header and payload
    iat = int(datetime.now().timestamp())

    header = {"alg": "HS256", "typ": "JWT", "kid": id}
    payload = {"iat": iat, "exp": iat + 5 * 60, "aud": "/admin/"}

    # Create the token (including decoding secret)
    token = jwt.encode(
        payload, bytes.fromhex(secret), algorithm="HS256", headers=header
    )

    # Make an authenticated request to create a post
    url = f"{config.GHOST_DOMAIN}/ghost/api/admin/posts/?source=html"
    headers = {"Authorization": "Ghost {}".format(token)}
    html = markdown.markdown(data["markdown"])
    html = html.replace(
        "<YOUTUBE_EMBED_PLACEHOLDER>",
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    )
    html = html.replace(
        "THUMBNAIL_PLACEHOLDER_URL",
        f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
    )
    body = {"posts": [{"title": data["title"], "html": html}]}
    r = requests.post(url, json=body, headers=headers)

    try:
        db.session.add(video)
        db.session.commit()
        return {"code": "success"}
    except Exception as e:
        return {"code": "error", "message": str(e)}


@celery.task
def prepare_video_transcript(video_url):
    w = Worker(assembly_ai_api_key=config.ASSEMBLY_AI_KEY).start(video_url)


@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500
