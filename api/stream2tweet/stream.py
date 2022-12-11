headers = {"authorization": api_token}
with open(self.filename, "rb") as audio_bytes:  # read the binary data from a wav file
    data = audio_bytes.read()[44:]  # strip off wav headers
data = base64.b64encode(
    data
)  # base64 encode the binary data so it can be included as a JSON parameter
data = str(data, "utf-8")
json = {"audio_data": data}
response = requests.post(
    "https://api.assemblyai.com/v2/stream", json=json, headers=headers
)  # send the data to the /v2/stream endpoint
self.results = response.json()["text"]
