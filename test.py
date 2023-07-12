import requests

req = {
  "text": "This is an example sentence",
}

url = 'http://127.0.0.1:9696/predict'
response = requests.post(url, json=req)
print(response.json())
