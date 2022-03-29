class Customer(object):

    def __init__(self, name, order):
        self.name = name
        self.orders = order

    def __str__(self):
        return f'Orders for {self.name}:\n{self.orders}'
