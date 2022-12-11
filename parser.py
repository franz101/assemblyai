# %%
# %%
from markdownmaker.document import Document
from markdownmaker.markdownmaker import *
# %%
!pip install youtube-dl
# %%
import youtube_dl

# %%
import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        print(d)

ydl_opts = {
    'format': 'worstaudio/worst',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl' : './tmp/%(id)s.%(ext)s',
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

# %%
import sys
sys.path.insert(1, "./api")
from tube2blog.worker import Worker
w = Worker().start("https://www.youtube.com/watch?v=5GorMC2lPpk")
# %%
!pip install markdownmaker
# %%

import pathlib



# %%
""
# %%
pathlib.Path("./tmp/BawJenozKc.webm").with_suffix(".mp3")
# %%
