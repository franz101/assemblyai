from typing import Dict



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
    doc.add(Header(self.headline))
    if hasattr(self, "image"):
      doc.add(Image(url=self.image["url"], alt_text=self.image["alt_text"]))
    doc.add(Paragraph(self.paragraph))
    doc.add(Paragraph(self.bullets))
    return doc.write()

