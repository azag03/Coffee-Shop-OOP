from toolbox import is_number


class Product(object):

    def __init__(self, name, type, price):
        self._name = name
        self._type = type
        self._price = price

    def __str__(self):
        return f'{self._name} ({self._type}) ${self._price}/lb'

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    name = property(get_name)
    price = property(get_price)