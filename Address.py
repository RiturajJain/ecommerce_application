"""
This module defines the Address class.
"""

class Address:

    def __init__(self, street_address, city, state, country, pin_code):
        self.street_address = street_address
        self.city = city
        self.state= state
        self.country = country
        self.pin_code = pin_code

    # NOTE: getters and setters should be implemented for all the attributes.