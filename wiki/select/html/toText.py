import html2text

from .default import HTMLDefault


class HTMLToText(HTMLDefault):
    def __init__(self, response):
        super().__init__(response)
        self.handler = html2text.HTML2Text()

    def get(self):
        filtered_response = self.response
        for search_result in filtered_response:
            search_result['snippet'] = self.handler.handle(search_result['snippet']).replace('\n', '')
        return filtered_response
