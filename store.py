from product import Product
from customer import Customer
from order import Order
from address import Address
from shippingMethod import ShippingMethod
from lineItem import LineItem
from toolbox import get_integer, get_integer_between


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
        string = 'Customers:\n'
        for customer in self._currentCustomer:
            string += f'{customer}\n'
        string += '\nProducts'
        for product in self._products:
            string += f'{product}\n'
        string += '\nShipping Methods'
        for shippingMethod in self._shippingMethods:
            string += f'{shippingMethod}\n'
        return string

    def read_products(self, fileName):
        """Read the available products from a file, creates Product objects for them, and puts them in the product
        list."""
        inputFile = open(fileName, 'r')
        file = inputFile.read()
        for line in file.split('\n'):
            name, type, price = line.split(',')
            product = Product(name.strip(), type.strip(), float(price.strip()))
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
            shippingMethod = ShippingMethod(name.strip(), description.strip(), float(fixedCost.strip()),
                                            float(rate.strip()))
            try:
                self._shippingMethods.append(shippingMethod)
            except TypeError:
                print(f'{name} not added to inventory. Check {fileName}')

    def display_products(self):
        """Returns a string of products used to display the products."""
        productCounter = 0
        string = 'These are your product options:\n\n'
        for product in self._products:
            productCounter += 1
            string += f'  {productCounter}. {product}\n'
        print(string)

    def display_shipping_methods(self):
        """Returns a string of shipping methods used to display the shipping methods ."""
        shippingMethodCounter = 0
        string = 'Here are your shipping choices:\n\n'
        for shippingMethod in self._shippingMethods:
            shippingMethodCounter += 1
            string += f'  {shippingMethodCounter}. {shippingMethod}\n'
        print(string)

    def sales(self):
        """Returns the total dollar amount sold today."""
        totalSales = 0
        for customer in self._customers:
            for order in customer.ordersList:
                totalSales += order.total()
        print(f'Total Sales:      ${totalSales:8.2f}')

    def shipping(self):
        """Returns the total shipping amount today."""
        totalShipping = 0
        for customer in self._customers:
            for order in customer.ordersList:
                totalShipping += order.shipping()
        print(f'Total Shipping:   ${totalShipping:8.2f}')

    def tax(self):
        """Returns the total tax collected today."""
        totalTax = 0
        for customer in self._customers:
            for order in customer.ordersList:
                totalTax += order.tax()
        print(f'Total Tax:        ${totalTax:8.2f}')

    def add_customer(self):
        """Add a new customer. :return: None"""
        if self._currentCustomer is not None:
            print(f'Welcome back {self._currentCustomer.name}')
            print(self._currentCustomer)
        else:
            name = input('What is your name? ')
            self._currentCustomer = Customer(name)
            self.add_order()

            print(f'{self._currentCustomer}')
            self._customers.append(self._currentCustomer)

    def add_order(self):
        """Add an order to the current customer. :return: None"""
        if self._currentCustomer is not None:
            street, city, state, zipcode = self.get_address()
            address = Address(street, city, state, zipcode)

            shippingChoice = self.get_shipping_methods()
            shippingMethod = self._shippingMethods[shippingChoice-1]

            self._currentOrder = Order(address, shippingMethod)
            self.add_item()

            print(self._currentOrder)

            self._currentCustomer.ordersList.append(self._currentOrder)
            print(self._currentCustomer)
        else:
            print('You must create a customer before placing an order.')
            self.add_customer()

    def add_item(self):
        """Add an item to the current order. :return: None"""
        if self._currentOrder is not None:
            productChoice = self.get_products()
            amount = self.get_amount()
            lineItem = LineItem(self._products[productChoice-1], amount)
            self._currentOrder.lineItemList.append(lineItem)
        else:
            print('You must create an order before adding an item.')
            self.add_order()

    def get_address(self):
        street = input('On what street are you currently living? ')
        city = input('What city do you live in? ')
        state = input('What state do you live in? ').upper()
        while state not in Address.states:
            print('Address requires a valid 2 letter US state postal code.')
            state = input('What state do you live in? ').upper()
        zipcode = get_integer('What is your zipcode? ')
        while len(str(zipcode)) != 5:
            print('Zipcode requires 5 numbers.')
            zipcode = get_integer('What is your zipcode? ')
        return street, city, state, zipcode

    def get_amount(self):
        amount = get_integer('How much would you like (in lbs)? ')
        return amount

    def print_receipt(self):
        print(self._currentOrder)

    def get_products(self):
        self.display_products()
        productCounter = 0
        for product in self._products:
            productCounter += 1
        productChoice = get_integer_between(1, productCounter, 'Choose a product: ')
        return productChoice

    def get_shipping_methods(self):
        self.display_shipping_methods()
        shippingMethodCounter = 0
        for shippingMethod in self._shippingMethods:
            shippingMethodCounter += 1
        shippingChoice = get_integer_between(1, shippingMethodCounter, 'Pick a shipping method: ')
        return shippingChoice

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
                print('----------------------------')
                self.sales()
                self.tax()
                self.shipping()
                print('----------------------------')
            elif command == 'Q':
                finished = True
            else:
                raise TypeError('figure it out')
