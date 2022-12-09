from typing import Dict

# markdown parser
class ParseMarkDown:
    
    def add_summary(self, summary: Dict):
        self.summary = summary

    def add_infos(self, info: Dict):
        self.info = info

    def create_text(self):
        self.parse_summary(self.summary)
        self.parse_infos(self.info)

    def parse_summary(self,summary):
        texts = []
        for k,v in summary.items()
            texts.append(v)
        text = "\n".join(texts)

    def parse_infos(self,info):
        texts = []
        for k,v in info.items()
            texts.append(v)
        text = "\n".join(texts)
