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

    def _set_filename(self, d):
        if d["status"] == "finished":
            print("Done downloading, now converting ...")
            self.filename = pathlib.Path(d["filename"]).with_suffix(".mp3")

    def youtube_dl(self, url):
        ydl_opts = {
            "format": "worstaudio/worst",
            "cachedir": "./tmp/cache",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "progress_hooks": [self._set_filename],
            "outtmpl": "./tmp/%(id)s.%(ext)s",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return self.filename.stem, str(self.filename)
