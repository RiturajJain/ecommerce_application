"""
This module defines the ShoppingCart class.
"""

class ShoppingCart:

    def __init__(self, storage):
        self.storage = storage
        self.products = {}

    def add_product(self, product_id):
        if product_id not in self.storage.products:
            raise Exception(f"Product with product_id {product_id} doesn't exist")

        self.products[product_id] = self.products.get(product_id, 0) + 1

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise Exception(f"Product with product_id {product_id} is not present in the Shopping Cart!")

        self.products.pop(product_id)

    def update_product_quantity(self, product_id, quantity):
        current_quantity = self.products.get(product_id, 0)
        new_quantity = current_quantity + quantity
        if new_quantity < 0:
            raise Exception("Product Quantity cannot be less than zero!")
        elif new_quantity == 0:
            self.products.pop(product_id)
        else:
            self.products[product_id] = new_quantity

    def get_products(self):
        if not self.products:
            print("The Shopping cart is empty!")
        else:
            for product_id, quantity in self.products.items():
                product = self.storage.products[product_id]
                print(product)
                print(f"Quantity: {quantity}")

    def checkout(self):
        cost = 0
        for product_id, quantity in self.products.items():
            product = self.storage.products[product_id]
            cost += product.price * quantity

        self.products = {}
        print(f"Total Cost: {cost}")
