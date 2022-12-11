import yt_dlp
import re


def download_video(url):

    ydl_opts = {
        "format_sort": "360",
        "live-from-start": False,
        "force-overwrites": True,
        "continue_dl": True,
        "skip-unavailable-fragments": True,
        "outtmpl": "./tmp/%(id)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # extract youtube id with regex from url
    # example youtube url:
    # https://www.youtube.com/watch?v=NT2H9iyd-ms
    # https://www.youtu.be/NT2H9iyd-ms
    pattern = re.compile(
        r"(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/|user\/\w+\/\w+\/))([\w\-]{11})"
    )
    id = pattern.search(url).group(1)
    return id
