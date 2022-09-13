import requests
import json

BASE_URL = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "012993441012"}

response = requests.get(BASE_URL, params=parameters)
print(response.url, response.status_code)

content = response.content
info = json.loads(content)
brand = info["items"][0]["brand"]
title = info["items"][0]["title"]
print(title, brand)
