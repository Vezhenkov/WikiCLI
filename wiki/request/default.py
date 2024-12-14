import requests


class RequestDefault:
    def __init__(self, url_processor):
        self.url_processor = url_processor

    def get(self):
        return requests.get(self.url_processor.get()).json()
