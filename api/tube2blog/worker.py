from tube2blog.api import AssemblyAiAPI
from tube2blog.parser import Parser
from tube2blog.downloader import Downloader
from tube2blog.utils import find_type
import json 

class Worker:
  
  def __init__(self,assembly_ai_api_key="a6cc25c4b313444ebb1c12c1ad27d354"):
    self.a = AssemblyAiAPI(assembly_ai_api_key)
    self.d = Downloader()
    self.p = Parser()
  
  def start(self, youtube_url):
    print("Downloading video")
    file_id = self.d.fetch_yt(youtube_url)
    print("Converting video")
    audio_file_id = self.d.convert_to_mp3(file_id)
    print("Uploading file")
    audio_url = self.a.upload_file(audio_file_id)
    self.audio_url = audio_url
    print("Fetching transcripts")
    jobs = self.a.fetch_all_transcripts(audio_url)
    completed_jobs = []
    for job in jobs:
      print("Fetching jobs")
      job_id = job.get("id")
      if job_id:
        job["transcript"] = self.a.wait_for_job(job_id)
        with open(f"{job['type']}.json","w") as f:
          f.write(json.dumps(job))
        completed_jobs.append(job)

    print("creating files")
    bullets = find_type("type","bullets",completed_jobs)["transcript"]["summary"]
    bullets_verbose = find_type("type","bullets_verbose",
                                completed_jobs)["transcript"]["summary"]
    headline = find_type("type","headline",
                         completed_jobs)["transcript"]["summary"]
    paragraph = find_type("type","paragraph",
                          completed_jobs)["transcript"]["summary"]
    
    self.p.add_bullets(bullets_verbose)
    self.p.add_headline(headline)
    self.p.add_paragraph(paragraph)
    markdown  = self.p.create_document()
    with open("markdown.md","w") as f:
      f.write(markdown)
    return markdown
