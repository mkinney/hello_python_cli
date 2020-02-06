class Hello():

    def __init__(self, name):
        self.name = name
        self.title = ''

    def hello(self):
        title = ''
        if self.title:
            title = '{} '.format(self.title)
        return 'Hello {}{}'.format(title, self.name)
