from .default import RequestDefault


class RequestSearch(RequestDefault):
    def __init__(self, url_processor):
        super().__init__(url_processor)
        self.search_info_path = ['query', 'search']

    def get(self):
        search_info = super().get()
        for key in self.search_info_path:
            search_info = search_info[key]
        return search_info
