from address import Address

class Order(object):

    def __init__(self, lineItem, address, shippingMethod):
        self.lineItem = lineItem
        self.address = address
        self.shippingMethod = shippingMethod

    def __str__(self):
        string = f'Address:\n{self.address}\n\n'
        string += 'Item                 Cost       Amount       Total\n'
        string += '--------------------------------------------------\n'
        string += f'{self.lineItem}\n'
        string += '--------------------------------------------------\n'
        string += f'Tax: ${self.tax():0.2f}\n'
        string += f'Shipping: ${self.shipping():0.2f}\n'
        string += f'Total: ${self.total():0.2f}'
        return string

    def tax(self):
        """Calculates the price plus tax for a product."""
        return self.address.tax_rate() * self.lineItem.cost()

    def shipping(self):
        """Calculates the shipping costs."""
        return self.shippingMethod.fixedCost + (self.shippingMethod.rate * self.lineItem.amount)

    def total(self):
        """Calculates the total cost of an order."""
        return self.lineItem.cost() + self.tax() + self.shipping()
