class Customer(object):

    @property
    def name(self):
        return self._name

    def __init__(self, name):
        self._name = name
        self.ordersList = []

    def __str__(self):
        string = f'Orders for {self._name}:\n'
        for order in self.ordersList:
            string += f'{order}\n'
        return string

    def get_name(self):
        return self._name

    name = property(get_name)