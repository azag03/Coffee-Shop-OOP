class LineItem(object):

    def __init__(self, product, amount):
        self.product = product
        if amount > 0:
            self.amount = amount
        else:
            raise TypeError('Amount must be greater than zero.')

    def __str__(self):
        string = ''
        #
        # :20s adds 20 extra spaces to a variable
        # :0.2f adds 0 extra spaces and formats (only floats) to 2 decimal places
        #
        string += f'{self.product.name:20s} ${self.product.price:0.2f}  * {self.amount:5.2f}lbs = ${self.cost():7.2f}'
        return string

    def cost(self):
        """Calculates the cost for the amount of a specific product."""
        return self.product.price * self.amount
