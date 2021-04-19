"""
This module defines the Account class which is used to model the user's account in the ecommerce app. This class can be inherited by different types of users like customer, admin etc. if required in the future.
"""

class Account:

    def __init__(self, user_id, password, name, address, date_of_birth):
        # NOTE: user_id should be unique (like email).
        self._id = user_id
        # NOTE: The password should be encrypted instead of storing in raw form.
        self.password = password
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth

    # NOTE: getters and setters should be implemented for all the attributes.
