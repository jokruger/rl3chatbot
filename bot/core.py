class Option():
    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body

class Answer():
    def __init__(self, message=None, options=None, stop=False):
        self.message = message
        self.options = options
        self.stop = stop
