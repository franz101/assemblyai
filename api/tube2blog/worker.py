from tube2blog.api import AssemblyAiAPI
from tube2blog.parser import Parser
from tube2blog.downloader import Downloader
from tube2blog.utils import find_type
import json
import requests

HOST = "http://localhost:5000"


class Worker:
    def __init__(self, assembly_ai_api_key="a6cc25c4b313444ebb1c12c1ad27d354"):
        self.a = AssemblyAiAPI(assembly_ai_api_key)
        self.d = Downloader()
        self.p = Parser()

    def status_update(self, id, payload):
        try:
            requests.post(f"{HOST}/api/update_video_status/{id}", json=payload)
        except Exception as e:
            print(e)

    def start(self, youtube_url):

        print("Downloading video")

        video_id, file_id = self.d.youtube_dl(youtube_url)
        print("Uploading file")
        self.status_update(
            video_id,
            {
                "status": "processing",
                "transcript": "",
                "markdown": "markdown",
                "html": "html",
                "title": "title",
            },
        )
        audio_url = self.a.upload_file(file_id)
        self.audio_url = audio_url
        print("Fetching transcripts")
        jobs = self.a.fetch_all_transcripts(audio_url)
        completed_jobs = []
        for job in jobs:
            print("Fetching jobs")
            job_id = job.get("id")
            if job_id:
                job["transcript"] = self.a.wait_for_job(job_id)
                with open(f"tmp/{job['type']}.json", "w") as f:
                    f.write(json.dumps(job))
                completed_jobs.append(job)

        print("creating files")
        # bullets = find_type("type", "bullets", completed_jobs)["transcript"]["summary"]
        bullets_verbose = find_type("type", "bullets_verbose", completed_jobs)[
            "transcript"
        ]["summary"]
        headline = find_type("type", "headline", completed_jobs)["transcript"][
            "summary"
        ]
        paragraph = find_type("type", "paragraph", completed_jobs)["transcript"]["text"]
        self.p.add_bullets(bullets_verbose)
        self.p.add_headline(headline)
        self.p.add_image("THUMBNAIL_PLACEHOLDER_URL")
        self.p.add_paragraph(paragraph)
        markdown = self.p.create_document()
        with open("tmp/markdown.md", "w") as f:
            f.write(markdown)
        self.status_update(
            video_id,
            {
                "status": "finished",
                "transcript": paragraph,
                "markdown": markdown,
                "title": headline,
            },
        )

        return markdown
