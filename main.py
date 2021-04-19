"""
This module contains code to start the Application and initialize it with some dummy data.
It can be extended to take the input from the User.

Key Points to Note:

1. At most places, I have raise and caught general Exception for simplicity purpose. But in a real system, this should be avoided as it can hide some bugs and make difficult to debug. Instead, specific or custom exceptions should be defined and used.
2. Getters and Setters should be defined for all the attributes in a class. They have been avoided here for simplicity.
"""
from Address import Address
from ECommerceSystem import ECommerceSystem
from Product import Product
from Storage import Storage
from User import User
from UserAuthSystem import UserAuthSystem

if __name__ == "__main__":
    storage = Storage.get_instance()
    user_auth = UserAuthSystem(storage)
    address = Address("No. 5, 5th Main, Domlur 2nd Stage", "Bangalore", "Karnataka", "India", 560071)
    user = User("rituraj.jain2020@gmail.com", "randompass", "Rituraj Jain", address, "23-07-1998")
    product1 = Product("Moto G8 PowerLite", "Great phone at an affordable price", 10500)
    product2 = Product("Mi 4A PRO Android LED TV", "80 cm (32 inches) HD Ready | Black", 14999)
    product3 = Product("Fastrack reflex 3.0", "Full touch, color display, Heart rate monitor, Dual- tone silicone strap and up to 10 days battery life", 2495)

    storage.add_user(user)
    storage.add_product(product1)
    storage.add_product(product2)
    storage.add_product(product3)
    
    ecommerce_system = ECommerceSystem(storage, user_auth)
    ecommerce_system.start()