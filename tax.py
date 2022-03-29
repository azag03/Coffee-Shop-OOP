class Tax(object):

    def __init__(self, state, taxRate):
        self.state = state
        self.taxRate = taxRate

    def __str__(self):
        string = ''
        string += f'{self.state}: '
        return string