"""
This module defines the Storage class which acts as an in-memory database
for the ecommerce application. Singleton Pattern is used to implement Storage class.
"""

class Storage:

    instance = None

    def __init__(self):
        if Storage.instance is None:
            self.users = {}
            self.products = {}
            self.current_user = None
            Storage.instance = self
        else:
            raise Exception("Only a Single instance of this class can be created!")

    @staticmethod
    def get_instance():
        if Storage.instance is None:
            Storage()
        return Storage.instance

    def add_user(self, user):
        self.users[user._id] = user

    def add_product(self, product):
        self.products[product._id] = product