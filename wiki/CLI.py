from .client_input.default import ClientInputDefault
from .url.query import URLQuery
from .request.search import RequestSearch
from .select.page_id import SelectPageID
from .url.page import URLPage
from .browser.default import BrowserDefault


class CLI:
    def __init__(self):
        self.client_input = ClientInputDefault()
        self.url_query = URLQuery(self.client_input)
        self.request = RequestSearch(self.url_query)
        self.select = SelectPageID(self.request)
        self.url_page = URLPage(self.select)
        self.browser = BrowserDefault(self.url_page)

    def get(self):
        return self.browser.get()
