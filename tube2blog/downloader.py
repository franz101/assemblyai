import uuid
from pytube import YouTube

class Downloader:
    def __init__(self,url= "https://www.youtube.com/watch?v=NT2H9iyd-ms"):
        youtube_video = YouTube(url)
        streams = youtube_video.streams.filter(only_audio=True)
        stream = streams.first()
        uid = uuid.uuid4().hex
        stream.download(filename=uid)
        return uid