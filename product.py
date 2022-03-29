from toolbox import is_number


class Product(object):

    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def __str__(self):
        return f'{self.name} ({self.type}) ${self.price}/lb'
