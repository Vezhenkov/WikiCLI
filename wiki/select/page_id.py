from .default import SelectDefault


class SelectPageID(SelectDefault):
    def __init__(self, request):
        super().__init__(request)
        self.page_info_path = ['pageid']

    def get(self):
        page_info = super().get()
        for key in self.page_info_path:
            page_info = page_info[key]
        return page_info
