from toolbox import is_number


class ShippingMethod(object):

    def __init__(self, name, description, fixedCost, rate):
        self._name = name
        self._description = description
        self._fixedCost = fixedCost
        self._rate = float(rate)

    def __str__(self):
        return f'{self._name} ({self._description}): ${self._fixedCost} + ${self._rate}/lb.'

    def get_name(self):
        return self._name

    def get_fixed_cost(self):
        return self._fixedCost

    def get_rate(self):
        return self._rate

    name = property(get_name)
    fixedCost = property(get_fixed_cost)
    rate = property(get_rate)