import base64
import requests
import time


class HuggingfaceApi:
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "tomofi-easyocr.hf.space",
        "Origin": "https://tomofi-easyocr.hf.space",
        "Referer": "https://tomofi-easyocr.hf.space/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    }
    api_url = "https://tomofi-easyocr.hf.space/api"

    def add_job(self, base64jpg):
        payload = {
            "data": ["data:image/jpeg;base64," + base64jpg.decode(), ["en"]],
            "session_hash": "rrvf79b7i7s",
            "action": "predict",
        }
        r = requests.post(
            f"{self.api_url}/queue/push/",
            json=payload,
            headers=self.headers,
            cookies={},
            auth=(),
        )
        return r.json().get("hash")

    def get_job(self, job_hash):
        payload = {"hash": job_hash}
        r = requests.get(
            f"{self.api_url}/queue/status",
            json=payload,
            headers=self.headers,
            cookies={},
            auth=(),
        )
        return r.json()

    def wait_for_job(self, job_hash):
        status = self.get_job(job_hash)
        while status.get("status") not in ["FAILED", "COMPLETE"]:
            time.sleep(1)
            status = self.get_job(job_hash)
        return status

    def ocr_image(self, image_path):
        with open(image_path, "rb") as image_file:
            base64jpg = base64.b64encode(image_file.read())
        job_hash = self.add_job(base64jpg)
        return job_hash

    def parse_result(self, result):
        arr = result.get("data", {}).get("data", [None, {}])[1].get("data", [[]])
        ocr = " ".join(list(map(lambda x: next(iter(x)), arr)))
        return ocr
