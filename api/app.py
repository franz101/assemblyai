import requests, config
from flask import Flask
from googleapiclient.discovery import build
from utils.YTStats import YTstats

app = Flask(__name__)

@app.route("/")
def fetch_videos():

    #youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)

    channel_id = "UCY2ifv8iH1Dsgjrz-h3lWLQ"

    yt = YTstats(config.YOUTUBE_API_KEY, channel_id)
    yt.extract_all()
    yt.dump()  # dumps to .json
    
    response = "success"
    return response
