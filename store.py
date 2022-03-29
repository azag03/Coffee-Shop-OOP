from product import Product
from customer import Customer
from order import Order
from shippingMethod import ShippingMethod
from toolbox import get_integer_between


class Store(object):

    def __init__(self):
        self._customers = []
        self._products = []
        self.read_products('inventory.txt')
        self._shippingMethods = []
        self.read_shipping_methods('shipping.txt')
        self._currentCustomer = None
        self._currentOrder = None

    def __str__(self):
        """Returns a string containing the products, shipping methods and customers of the store."""
        pass

    def read_products(self, fileName):
        """Read the available products from a file, creates Product objects for them, and puts them in the product
        list."""
        inputFile = open(fileName, 'r')
        file = inputFile.read()
        for line in file.split('\n'):
            name, type, price = line.split(',')
            product = Product(name.strip(), price.strip(), type.strip())
            try:
                self._products.append(product)
            except TypeError:
                print(f'{name} not added to inventory. Check {fileName}')

    def read_shipping_methods(self, fileName):
        """Read the available products from a file., creates ShippingMethod objects for them, and puts them in the
        shipping methods list."""
        inputFile = open(fileName, 'r')
        file = inputFile.read()
        for line in file.split('\n'):
            name, description, fixedCost, rate = line.split(',')
            shippingMethod = ShippingMethod(name.strip(), description.strip(), fixedCost.strip(), rate.strip())
            try:
                self._shippingMethods.append(shippingMethod)
            except TypeError:
                print(f'{name} not added to inventory. Check {fileName}')

    def display_products(self):
        """Returns a string of products used to display the products."""
        string = "These are our product options:\n\n"
        string += "   1. Columbian Roast (coffee): $8.45/lb\n"
        string += "   2. Pumpkin Spice (coffee): $10.35/lb\n"
        string += "   3. Jedi Java (coffee): $13.25/\n"
        string += "   4. Tastea (tea): $6.75/lb\n"
        string += "   5. Earl Grey (tea): $4.50/lb\n"
        string += "   6. Westminster Queen's Choice (tea): $ 1.95/lb\n"
        print(string)

    def display_shipping_methods(self):
        """Returns a string of shipping methods used to display the shipping methods ."""
        string = "These are your shipping choices:\n\n"
        string += "   1. Standard Shipping (normal shipping method): $4.50 + $1.86/lb\n"
        string += "   2. FedEx (faster but more expensive): $4.65/lb\n"
        string += "   3. UPS (less expensive; for very large orders): $12.00 + $0.95/lb\n"
        print(string)

    def sales(self):
        """Returns the total dollar amount sold today."""
        totalSales = 0
        for customer in self._customers:
            totalSales += 0
        return totalSales

    def shipping(self):
        """Returns the total shipping amount today."""
        totalShipping = 0
        for shippingMethod in self._shippingMethods:
            totalShipping += 0
        return totalShipping

    def tax(self):
        """Returns the total tax collected today."""
        totalTax = 0
        return totalTax

    def add_customer(self):
        """Add a new customer. :return: None"""
        if self._currentCustomer is not None:
            print(f'Welcome back {self._currentCustomer.name}')
            print(self._currentCustomer)
        else:
            name = input('What is your name? ')
            order = None
            self._currentCustomer = Customer(name, order)
            print(self._currentCustomer)
            self._customers.append(self._currentCustomer)

    def add_order(self):
        """Add an order to the current customer. :return: None"""
        if self._currentCustomer is not None:
            print(f'Welcome back {self._currentCustomer.name}')
            address = input('What is your address? ')
            self.display_shipping_methods()
            shippingMethod = get_integer_between(1, 3, 'Pick a shipping method: ')
            if shippingMethod == 1:
                shippingInfo = ShippingMethod('Standard Shipping', 'normal shipping method', 4.50, 1.86)
            elif shippingMethod == 2:
                shippingInfo = ShippingMethod('FedEx', 'faster but more expensive', 0.00, 4.65)
            elif shippingMethod == 3:
                shippingInfo = ShippingMethod('UPS', 'less expensive; for very large orders', 12.00, 0.95)
            lineItem = None
            self._currentOrder = Order(lineItem, address, shippingInfo)
            print(self._currentOrder)
            self._currentCustomer.order = self._currentOrder
        else:
            print('You must create a customer before placing an order.')
            self.add_customer()

    def add_item(self):
        """Add an item to the current order. :return: None"""
        #
        # Check to see if there is an order to add an item to. Create one if noe (or error out)
        #

        #
        # Create a new lineItem object and add it to the current order
        #

    def print_receipt(self):
        print(self._currentOrder.receipt())

    def get_products(self):
        return self._products

    def get_shipping_methods(self):
        return self._shippingMethods

    def get_customers(self):
        return self._customers

    products = property(get_products)
    shippingMethods = property(get_shipping_methods)
    customers = property(get_customers)

    def run(self):
        commandString = 'ADD: [C]ustomer  [O]rder  [I]tem   PRINT: [R]eciept  [T]otals   [Q]UIT\n'
        print(commandString)
        validCommands = 'COIRTQ'
        finished = False
        while not finished:
            prompt = "What method would you like to complete? "
            command = input(prompt).upper()
            while command not in validCommands:
                prompt += '(please respond with a letter) '
                command = input(prompt).upper()
            if command == 'C':
                self.add_customer()
            elif command == 'O':
                self.add_order()
            elif command == 'I':
                self.add_item()
            elif command == 'R':
                self.print_receipt()
            elif command == 'T':
                self.sales()
            elif command == 'Q':
                finished = True
            else:
                raise TypeError('figure it out')
