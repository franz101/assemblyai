from app import db
from dataclasses import dataclass

@dataclass
class VideoQueue(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    video_id:str = db.Column(db.String, nullable=False)
    transcript:str = db.Column(db.String)
    markdown:str = db.Column(db.String)
    status:str = db.Column(db.String)
    queued_timestamp:int = db.Column(db.Integer)
    finished_timestamp:int = db.Column(db.Integer)