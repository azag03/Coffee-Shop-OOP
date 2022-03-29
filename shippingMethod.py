from toolbox import is_number


class ShippingMethod(object):

    def __init__(self, name, description, fixedCost, rate):
        self.name = name
        self.description = description
        self.fixedCost = fixedCost
        self.rate = float(rate)

    def __str__(self):
        return f'{self.name} ({self.description}): ${self.fixedCost} + ${self.rate}/lb.'
