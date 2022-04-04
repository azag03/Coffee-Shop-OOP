class Order(object):

    def __init__(self, address, shippingMethod):
        self.lineItemList = []
        self._address = address
        self._shippingMethod = shippingMethod

    def __str__(self):
        string = f'Address:\n{self._address}\n\n'
        string += 'Item                             Cost      Amount             Total\n'
        string += '-------------------------------------------------------------------\n'
        for item in self.lineItemList:
            string += f'{item}\n'
        string += '-------------------------------------------------------------------\n'
        string += f'{self.weight():46.2f} lbs    =    ${self.items_cost():7.2f}\n\n'
        string += f'                                                      Tax: ${self.tax():7.2f}\n'
        string += f'                                                 Shipping: ${self.shipping():7.2f}\n'
        string += f'                                                    Total: ${self.total():7.2f}\n'
        string += '-------------------------------------------------------------------'
        return string

    def items_cost(self):
        """Calculates the total cost for every item within the order (without tax or shipping)."""
        cost = 0
        for item in self.lineItemList:
            cost += item.cost()
        return cost

    def weight(self):
        """Calculates the total pounds for all items within an order."""
        amount = 0
        for item in self.lineItemList:
            amount += item.amount
        return amount

    def tax(self):
        """Calculates the tax for a product."""
        return self._address.tax_rate() * self.items_cost()

    def shipping(self):
        """Calculates the shipping costs."""
        return self._shippingMethod.fixedCost + (self._shippingMethod.rate * self.weight())

    def total(self):
        """Calculates the total cost of an order."""
        return self.items_cost() + self.tax() + self.shipping()
