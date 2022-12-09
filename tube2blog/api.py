import requests
import time
from tube2blog.utils import read_file


class AssemblyAiAPI:
    api_url = "https://api.assemblyai.com/v2"

    def __init__(self, API_KEY: str):
        self.create_headers(API_KEY)

    def create_headers(self, API_KEY: str):
        self.headers = {"Authorization": API_KEY}

    def get_transcript(self, id: str):
        r = requests.get(f"{self.api_url}/transcript/{id}", headers=self.headers)
        return r.json()

    def get_analysis(self, audio_url: str):
        payload = {
            "audio_url": audio_url,
            "sentiment_analysis": True,
            "entity_detection": True,
            "auto_chapters": True,
            "iab_categories": True,
            "content_safety": True,
            "auto_highlights": True,
        }
        r = requests.post(
            f"{self.api_url}/transcript", headers=self.headers, json=payload
        )
        j = r.json()
        return j["id"]

    def get_summary(self, audio_url: str):
        payload = {
            "audio_url": audio_url,
            "summarization": True,
            "summary_type": "bullets",
            "summary_model": "informative",
        }
        r = requests.post(
            f"{self.api_url}/transcript", headers=self.headers, json=payload
        )
        j = r.json()
        return j["id"]

    def upload_file(self, file_path):
        r = requests.post(
            f"{self.api_url}/upload", headers=self.headers, data=read_file(file_path)
        )
        j = r.json()
        return j["upload_url"]

    def wait_for_job(self, id):
        d = self.transcript(id)
        while d.get("status") == "processing":
            time.sleep(1)
            d = self.transcript(id)
        return d
