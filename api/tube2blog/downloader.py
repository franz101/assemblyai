import uuid
from pytube import YouTube
from moviepy.editor import *


class Downloader:
    def fetch_yt(self, url="https://www.youtube.com/watch?v=NT2H9iyd-ms") -> str:
        youtube_video = YouTube(url)
        streams = youtube_video.streams.filter(only_audio=True)
        stream = streams.first()
        uid = uuid.uuid4().hex
        stream.download(filename=uid)
        return uid

    def convert_to_mp3(self, uid: str, dir: str = ".") -> str:
        output_file = f"{dir}/{uid}.mp3"
        audio = AudioFileClip(uid)
        audio.write_audiofile(output_file)
        return output_file
