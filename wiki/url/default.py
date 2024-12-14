class URLDefault:
    def __init__(self, client_input):
        self.client_input = client_input
        self.url = 'https://ru.wikipedia.org/'

    def get(self):
        return self.url
