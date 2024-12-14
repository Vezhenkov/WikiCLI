from .default import URLDefault


class URLPage(URLDefault):
    def __init__(self, client_input):
        super().__init__(client_input)
        self.url = 'https://ru.wikipedia.org/w/index.php?curid={}'

    def get(self):
        return self.url.format(self.client_input.get())
