from .default import URLDefault


class URLQuery(URLDefault):
    def __init__(self, client_input):
        super().__init__(client_input)
        self.url = 'https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch="{}"'

    def get(self):
        return self.url.format(self.client_input.get())
