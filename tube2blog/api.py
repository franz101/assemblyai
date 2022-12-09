import requests


class AssemblyAiAPI:
    endpoint = "https://api.assemblyai.com/v2/transcript"

    def __init__(self, API_KEY: str):
        self.create_headers(API_KEY)

    def create_headers(API_KEY:str):
        self.header = {
            "Authorization": API_KEY,
            "Content-Type": "application/json"
            }

    def transcript(payload):
        id = requests.get(endpoint, headers=headers)

    def get_analysis():
        payload = {
            "sentiment_analysis": True,
            "entity_detection": True,
            "auto_chapters": True,
            "iab_categories": True,
            "content_safety": True,
            "auto_highlights": True
        }

    def get_summary():
        payload = {
            "summarization": True,
            "summary_type": "bullets",
            "summary_model":"informative"
        }
    
    def wait_for_job(id):



    username
    workers


    fetch status of this username_job_id:
    
