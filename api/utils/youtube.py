import requests
from bs4 import BeautifulSoup

def get_channel_id_from_handle(handle):
    source = requests.get(f"https://youtube.com/{handle}").text
    soup = BeautifulSoup(source, features="html.parser")
    links = soup.findAll("link")
    channel_url = None
    for link in links:
        if link.has_attr('href') and 'https://www.youtube.com/channel/' in link.get('href'):
            channel_url = link.get('href')
            break

    if channel_url is None:
        return None

    try:
        channel_id = channel_url.split('/')[-1]
    except:
        return None

    return channel_id