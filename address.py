class Address(object):

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    taxes = {"AL": .04, "AK": 0, "AZ": .056, "AR": .065, "CA": .0725, "CO": .029, "CT": .0635, "DC": .0575, "DE": 0,
             "FL": .06, "GA": .04, "HI": .04, "ID": .06, "IL": .0625, "IN": .07, "IA": .06, "KS": .065, "KY": .06,
             "LA": .05, "ME": .055, "MD": .06, "MA": .0625, "MI": .06, "MN": .06875, "MS": .07, "MO": .04225, "MT": 0,
             "NE": .05, "NV": .0685, "NH": 0, "NJ": .06875, "NM": .05125, "NY": .04, "NC": .0475, "ND": .05,
             "OH": .0575, "OK": .045, "OR": 0, "PA": .06, "RI": .07, "SC": .06, "SD": .045, "TN": .07, "TX": .0625,
             "UT": .0595, "VT": 0, "VA": .053, "WA": .065, "WV": .06, "WI": .05, "WY": .04}

    def __init__(self, street, city, state, zipcode):
        self._street = street
        self._city = city
        if state in Address.states:
            self._state = state
        else:
            raise TypeError('Address requires a valid 2 letter US state postal code.')
        self._zipcode = zipcode

    def __str__(self):
        return f'{self._street}\n{self._city}, {self._state} {self._zipcode}'

    def tax_rate(self):
        return Address.taxes[self._state]

    def get_state(self):
        return self._state

    state = property(get_state)
