from __future__ import unicode_literals
import uuid
import youtube_dl
from pytube import YouTube
from moviepy.editor import *
import pathlib


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

    def youtube_dl(self, url):
        filename = ""

        def my_hook(d):
            if d["status"] == "finished":
                print("Done downloading, now converting ...")
                filename = pathlib.Path(d["filename"]).with_suffix("mp3")

        ydl_opts = {
            "format": "worstaudio/worst",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "progress_hooks": [my_hook],
            "outtmpl": "./tmp/%(id)s.%(ext)s",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return filename
