"""
This module defines the Product class used to model the product in the ecommerce app.
This class can be extended to add other attributes like category, quantity, reviews etc.
"""

class Product:

    product_id = 1
    def __init__(self, name, description, price):
        # NOTE: The product_id should be unique and autogenerated
        self._id = Product.product_id
        Product.product_id += 1
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product ID: {self._id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}"

    # NOTE: getters and setters should be implemented for all the attributes.
