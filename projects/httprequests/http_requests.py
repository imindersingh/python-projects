import json
import requests


class HttpRequests:
    def __init__(self, base_url, parameters):
        self.base_url = base_url
        self.parameters = parameters

    def get(self):
        return requests.get(url=self.base_url, params=self.base_url)

    def post(self, body):
        return requests.post(url=self.base_url, params=self.parameters, data=body)

    def getJsonBody(self, resp):
        return json.load(resp)
