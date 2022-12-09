import requests, config
from flask import Flask, abort, request, jsonify
from googleapiclient.discovery import build
from utils.youtube import get_channel_id_from_handle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/verify_handle/<handle>")
def verify_channel(handle="@parttimelarry"):
    channel_id = get_channel_id_from_handle(handle)

    if channel_id is None:
        abort(500)

    return {
        "code": "success",
        "channel_id": channel_id
    }

@app.route("/fetch_channel_videos/<channel_id>")
def fetch_channel_videos(channel_id):
    page = request.args.get('page', 1)

    url = f"https://www.googleapis.com/youtube/v3/search?key={config.YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    r = requests.get(url)
   
    return r.json()

@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500