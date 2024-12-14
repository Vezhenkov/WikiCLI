import prettytable

from ..html.toText import HTMLToText


class DisplayDefault:
    def __init__(self, select):
        self.select = select
        self.html_class = HTMLToText
        self.keys = ['title', 'snippet']
        self.sizes = [20, 60]
        self.prompt = 'Select article using keyboard arrows and enter'

    def get(self):
        assert len(self.keys) == len(self.sizes)
        response = self.get_response()
        table = self.get_table(response)
        return f'{self.prompt}\n{table}'

    def get_response(self):
        response = [{key: i[key] for key in self.keys} for i in self.select.response]
        response = self.html_class(response).get()
        return response

    def get_table(self, response):
        table = prettytable.PrettyTable(self.keys)
        table._max_width = {k: s for k, s in zip(self.keys, self.sizes)}
        table._min_width = {k: s for k, s in zip(self.keys, self.sizes)}
        table.align = 'l'
        table.valign = 'm'
        table.align[self.keys[0]] = 'c'
        table.header = False
        table.add_row(response[self.select.selected].values())
        return table
