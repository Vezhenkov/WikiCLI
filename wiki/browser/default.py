import webbrowser


class BrowserDefault:
    def __init__(self, url):
        self.url = url

    def get(self):
        return webbrowser.open(self.url.get())
