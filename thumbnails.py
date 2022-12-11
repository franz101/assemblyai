# %%
# Imports
import yt_dlp
import re
import glob
import subprocess
from api.tube2blog.huggingface import HuggingfaceApi
from api.tube2blog.cohere import CohereAPI
import pathlib

# %%
# Download thumbnails
def download_video(url):
    # extract youtube id with regex from url
    # example youtube url:
    # https://www.youtube.com/watch?v=NT2H9iyd-ms
    # https://www.youtu.be/NT2H9iyd-ms
    pattern = re.compile(
        r"(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/|user\/\w+\/\w+\/))([\w\-]{11})"
    )
    id = pattern.search(url).group(1)
    cleaned_url = "https://www.youtube.com/watch?v=" + id
    ydl_opts = {
        "format_sort": "360",
        "live-from-start": False,
        "force-overwrites": True,
        "continue_dl": True,
        "skip-unavailable-fragments": True,
        "outtmpl": "./tmp/%(id)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([cleaned_url])

    return id


url = "https://www.youtu.be/gfwNK3o45ng"
id = download_video(url)
#%%

# create thumbnails


def create_thumbnails(id):
    filename = "./tmp/" + id + ".webm"
    cmd = (
        "ffprobe -i "
        + filename
        + ' -show_entries format=duration -v quiet -of csv="p=0"'
    )
    duration = subprocess.check_output(cmd, shell=True)
    total_screenshots = 4
    duration = float(duration.decode("utf-8").strip())
    interval = 1 / (duration / total_screenshots)
    cmd = (
        "ffmpeg -i "
        + filename
        + " -vf fps="
        + str(interval)
        + " ./tmp/thumb_"
        + id
        + "_%d.jpg"
    )
    subprocess.call(cmd, shell=True)


id = "gfwNK3o45ng"
create_thumbnails(id)


# %%
# OCR thumbnails
files = glob.glob("./tmp/thumb_" + id + "_*.jpg")
h = HuggingfaceApi()
hashes = [{"file": file, "hash": h.ocr_image(file)} for file in files]
results = []
for hash in hashes:
    try:
        hash_id = hash.get("hash")
        if hash_id:
            job = h.wait_for_job(hash_id)
            parsed_ocr = h.parse_result(job)
            # write ocr to file in md file
            file_path = pathlib.Path(hash.get("file")).with_suffix(".md")
            with open(file_path, "w") as f:
                f.write(parsed_ocr)

            hash["parsed"] = parsed_ocr
            results.append(hash)
    except AssertionError:
        continue
# %%


# %%

# %%
# Generate tags

c = CohereAPI("API_KEY")

print("generating tags")


# %%
text_input = """How to find earnings and news data, and maybe we'll even classify some of this data as well. Show us how to fetch news using the Alpaca News API. Also show you how to use the free y finance package to fetch data from Yahoo. And maybe we can dive into this a little bit more in the future if we start diving into machine learning.
A headline on Arkinvest says it sees Tesla driving EV stock to $4,600 a share. That sounds very positive, but it labels it as negative. Maybe the move is to do the opposite of what Cathy Wood says.
Real time streaming news over WebSockets. Once you're connected and authenticated, you just need to subscribe to any stock or crypto symbols that you're interested in getting news about. Here's how it looks when you start receiving news.
In the next video in this series, we'll take a look at this Quant Rocket article that discusses whether to buy or sell stocks at Gap, up or down. Then we'll write some code to actually place some trades based on this article."""
headline = c.headline_generator(text_input)
print("Generated headline with cohere:")
print("Input:")
print(text_input)
print("Output:")
print(headline)

# %%
tags = c.tag_generator(text_input)
print("Generated tags with cohere:")
print(tags)
# %%
tutorial = c.tutorial_classifier(text_input)
print("Classified video type with cohere:")
print(tutorial)

# %%
