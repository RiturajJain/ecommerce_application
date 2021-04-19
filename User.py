"""
This module defines the User class which is used to model the user in the ecommerce app. It inherits from the Account class.
"""
from Account import Account
from ShoppingCart import ShoppingCart
from Storage import Storage

class User(Account):

    def __init__(self, user_id, password, name, address, date_of_birth):
        super().__init__(user_id, password, name, address, date_of_birth)
        self.cart = ShoppingCart(Storage.get_instance())

    # NOTE: getters and setters should be implemented for all the attributes.
