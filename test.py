import requests
from scr.config.config import load_configz

webhook_url = "http://localhost:5678/webhook-test/a3940b3d-1a6e-4a70-87b6-b2f4eeeafbe6"

data = {"id": 719467479, "text": "test1"}

response = requests.post(webhook_url, json=data)
print(response.status_code)
