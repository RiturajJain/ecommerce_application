"""
This module defines the UserAuthSystem class which is responsible for user sign up, login and logout. Singleton Pattern is used to implement UserAuthSystem class.
"""

class UserAuthSystem:

    instance = None

    def __init__(self, storage):
        if UserAuthSystem.instance is None:
            self.storage = storage
            UserAuthSystem.instance = self
        else:
            raise Exception("Only a Single instance of this class can be created!")

    @staticmethod
    def get_instance():
        if UserAuthSystem.instance is None:
            UserAuthSystem()
        return UserAuthSystem.instance

    def signup(self, user):
        if self.storage.current_user is not None:
            raise Exception(f"{self.storage.current_user.name} is already logged in!")

        if user._id in self.storage.users:
            raise Exception("User with given user_id already exists!")

        self.storage.users[user._id] = user

    def login(self, user_id, password):
        if self.storage.current_user is not None:
            raise Exception(f"{self.storage.current_user.name} is already logged in!")

        user = self.storage.users.get(user_id)
        if not user:
            raise Exception("User with given user_id doesn't exist!")

        if user.password != password:
            raise Exception("Incorrect Password!")

        self.storage.current_user = user

    def logout(self):
        # Empty the current user's shopping cart
        self.storage.current_user.cart.products = {}
        self.storage.current_user = None
