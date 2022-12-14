from typing import Dict
import json
from markdownmaker.document import Document
from markdownmaker.markdownmaker import *


class Parser:
    def add_bullets(self, summary):
        self.bullets = summary

    def add_headline(self, summary):
        self.headline = summary

    def add_image(self, image):
        self.image = image

    def add_paragraph(self, summary):
        self.paragraph = summary

    def create_document(self):
        doc = Document()

        if hasattr(self, "image"):
            doc.add(Image(url=self.image["url"], alt_text=self.image["alt_text"]))
        with HeaderSubLevel(doc):
            doc.add(Header(self.headline))
        doc.add(Paragraph(self.bullets))
        doc.add(Paragraph("<YOUTUBE_EMBED_PLACEHOLDER>"))
        doc.add(Paragraph("Transcript:"))
        doc.add(Paragraph(self.paragraph))
        return doc.write()
