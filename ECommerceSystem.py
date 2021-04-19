"""
This module defines the ECommerceSystem class. Singleton Pattern is used to implement the ECommerceSystem class.

The user can perform the following operations in the ECommerce Application:

# 1. Sign up
# 2. Log in
# 3. Log out (user should be logged in)
# 4. Browse Products (user should be logged in)
# 5. Add Product to Shopping Cart (user should be logged in)
# 6. View Products in Shopping Cart (user should be logged in)
# 7. Remove Product from Shopping Cart (user should be logged in)
# 8. Update Quantity of Product in Shopping Cart (user should be logged in)
# 9. Checkout (user should be logged in)
# 10. Exit from the application
"""
from Address import Address
from User import User
from getpass import getpass

import sys

class ECommerceSystem:

    instance = None

    def __init__(self, storage, user_auth):
        if ECommerceSystem.instance is None:
            self.storage = storage
            self.user_auth = user_auth
            ECommerceSystem.instance = self
        else:
            raise Exception("Only a Single instance of this class can be created!")

    @staticmethod
    def get_instance():
        if ECommerceSystem.instance is None:
            ECommerceSystem()
        return ECommerceSystem.instance

    def signup(self):
        user_id = input("Enter the user_id: ")
        password = getpass("Enter the password: ")
        name = input("Enter the name: ")
        street_address = input("Enter the street address: ")
        city = input("Enter the city: ")
        state = input("Enter the state: ")
        country = input("Enter the country: ")
        pin_code = input("Enter the pin_code: ")
        address = Address(street_address, city, state, country, pin_code)
        date_of_birth = input("Enter the date of birth (DD-MM-YYYY): ")
        user = User(user_id, password, name, address, date_of_birth)
        try:
            self.user_auth.signup(user)
        except Exception as err:
            print(f"\nError: {err}")

    def login(self):
        user_id = input("Enter the user_id: ")
        password = getpass("Enter the password: ")
        try:
            self.user_auth.login(user_id, password)
            print(f"\nLogged in as {self.storage.current_user.name}!",)
        except Exception as err:
            print(f"\nError: {err}")

    def logout(self):
        self.user_auth.logout()
        print("\nLogged out!")

    def browse_products(self):
        for product in self.storage.products.values():
            print(product, end='\n\n')

    def add_product_to_shopping_cart(self):
        try:
            product_id = int(input("Enter the product_id of the product: "))
        except ValueError:
            print("Error: Integer value expected!")
        try:
            self.storage.current_user.cart.add_product(product_id)
        except Exception as err:
            print(f"\nError: {err}")

    def view_products_in_shopping_cart(self):
        self.storage.current_user.cart.get_products()

    def remove_product_from_shopping_cart(self):
        try:
            product_id = int(input("Enter the product_id of the product: "))
        except ValueError:
            print("Error: Integer value expected!")
        try:
            self.storage.current_user.cart.remove_product(product_id)
        except Exception as err:
            print(f"\nError: {err}")

    def update_product_quantity_in_shopping_cart(self):
        try:
            product_id = int(input("Enter the product_id of the product: "))
        except ValueError:
            print("Error: Integer value expected!")
        quantity = int(input("Enter the product quantity: "))
        try:
            self.storage.current_user.cart.update_product_quantity(product_id, quantity)
        except Exception as err:
            print(f"\nError: {err}")

    def checkout(self):
        self.storage.current_user.cart.checkout()

    def exit_app(self):
        print("Exiting Application ...")
        sys.exit()

    def execute_operation(self, operations):
        """
        This method is responsible to take the operation number
        as input from the user and execute it
        """
        for i, operation in enumerate(operations):
            print(f"{i+1}. {operation[0]}")

        selected_operation = input(f"\nEnter the operation number (between 1 and {len(operations)}): ")
        print()
        if selected_operation.isdigit():
            selected_operation = int(selected_operation)-1
            operations[selected_operation][1]()
        else:
            raise TypeError("Integer value expected!")

    def start(self):
        """
        This method acts as an entrypoint for the system.
        """
        print("\n---------- Welcome to the ECommerce Application ----------", end="\n\n")
        without_login_operations = (
            ("Sign up", self.signup),
            ("Log in", self.login),
            ("Exit", self.exit_app)
        )

        with_login_operations = (
            ("Log out", self.logout),
            ("Browse Products", self.browse_products),
            ("Add Product to Shopping Cart", self.add_product_to_shopping_cart),
            ("View Products in Shopping Cart", self.view_products_in_shopping_cart),
            ("Remove Product from Shopping Cart", self.remove_product_from_shopping_cart),
            ("Update Quantity of Product in Shopping Cart", self.update_product_quantity_in_shopping_cart),
            ("Checkout", self.checkout),
            ("Exit", self.exit_app)
        )
        while True:
            # If the user is currently logged in
            if self.storage.current_user:
                try:
                    self.execute_operation(with_login_operations)
                except TypeError as err:
                    print(f"\nError: {err}")
            else:
                try:
                    self.execute_operation(without_login_operations)
                except TypeError as err:
                    print(f"\nError: {err}")

            print("\n" + "=" * 40 + "\n")
