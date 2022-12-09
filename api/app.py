import requests, config
from flask import Flask
from googleapiclient.discovery import build
from utils.youtube import get_channel_id_from_handle

app = Flask(__name__)

@app.route("/")
def fetch_videos(handle="@parttimelarry"):
    channel_id = get_channel_id_from_handle(handle)

    if channel_id is None:
        return {
            "code": "error"
        }

    url = f"https://www.googleapis.com/youtube/v3/search?key={config.YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    r = requests.get(url)
   
    return r.json()
