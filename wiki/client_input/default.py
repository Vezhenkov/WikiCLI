class ClientInputDefault:
    def __init__(self):
        self.prompt = 'Query: '

    def get(self):
        return input(self.prompt)
