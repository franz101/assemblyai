import requests
import time

class AssemblyAiAPI:
    api_url = "https://api.assemblyai.com/v2"

    def __init__(self, API_KEY: str):
        self.create_headers(API_KEY)

    def create_headers(API_KEY:str):
        self.header = { "Authorization": API_KEY }

    def transcript(id:str):
        r =  requests.get(f"{api_url}/transcript",
        headers=self.headers)
        return r.json()

    def get_analysis(audio_url: str):
        payload = {
            "audio_url": audio_url,
            "sentiment_analysis": True,
            "entity_detection": True,
            "auto_chapters": True,
            "iab_categories": True,
            "content_safety": True,
            "auto_highlights": True
        }

    def get_summary():
        payload = {
            "audio_url" : audio_url,
            "summarization": True,
            "summary_type": "bullets",
            "summary_model":"informative"
        }

    def upload_file(file_path):
        r = requests.post(f'{self.api_url}/upload',
                        headers=self.headers,
                        data=read_file(filename))
        j = r.json()
        return j["upload_url"]

    
    def wait_for_job(id):
        d = self.transcript(id)
        while d.get("status") not in ["error", "completed"]:
            time.sleep(1)
            d = self.transcript(id)
        return d
        

