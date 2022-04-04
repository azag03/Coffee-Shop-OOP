class LineItem(object):

    def __init__(self, product, amount):
        self._product = product
        if amount > 0:
            self._amount = amount
        else:
            raise TypeError('Amount must be greater than zero.')

    def __str__(self):
        string = ''
        #
        # :20s adds 20 extra spaces to a variable
        # :0.2f adds 0 extra spaces and formats (only floats) to 2 decimal places
        #
        string += f'{self._product.name:30s} ${self._product.price:5.2f}  * {self._amount:5.2f} lbs    =    ' \
                  f'${self.cost():7.2f}'
        return string

    def cost(self):
        """Calculates the cost for the amount of a specific product."""
        return self._product.price * self._amount

    def get_amount(self):
        return self._amount

    amount = property(get_amount)