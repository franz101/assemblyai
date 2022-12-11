import requests, config
from flask import Flask, abort, request, jsonify
from utils.youtube import get_channel_id_from_handle
from flask_cors import CORS
from tube2blog.worker import Worker
from celery import Celery

app = Flask(__name__)
CORS(app)

# add celery config
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.get("/api/verify_handle/<handle>")
def verify_channel(handle="@parttimelarry"):
    channel_id = get_channel_id_from_handle(handle)

    if channel_id is None:
        abort(500)

    return {
        "code": "success",
        "channel_id": channel_id
    }

@app.get("/api/fetch_channel_videos/<channel_id>")
def fetch_channel_videos(channel_id):
    page = request.args.get('page', 1)

    url = f"https://www.googleapis.com/youtube/v3/search?key={config.YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    r = requests.get(url)
   
    return r.json()

@app.post("/api/enqueue_videos")
def enqueue_videos():
    # accepts json post with video_ids
    data = request.json

    video_urls = list(map(lambda id: f"https://www.youtube.com/watch?v={id}", data['video_ids']))

    for video_url in video_urls:
        prepare_video_transcript.delay(video_url)

    return video_urls 

@celery.task
def prepare_video_transcript(video_url):
    w = Worker(assembly_ai_api_key=config.ASSEMBLY_AI_KEY).start(video_url)

@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500
