
# Ecommerce Application
This is the low level design for a console based ECommerce Application

The application should be able to support the following features:

1.  Any user should be able to sign up, log in and log out.
    
2.  Logged-in users should be able to browse products.
    
3.  Logged-in user should have a shopping cart where the user should be able to add multiple products.
    
4.  User should have the ability to checkout and total payable should be displayed while checkout.
    
5.  User should have the following attributes: name, user id, address, date of birth.
    
6.  The product should have the following attributes: name, product id, description, and price.
    
7.  User and Product information should be persisted in-memory.
    
8.  The console should have an option for all the operation mentioned above.

## Start the Application:
Python 3.7+ is required to run this application. main.py is used to start the application and initialize some dummy data to interact with the application. To start the application, simply run the following command:

    python3 main.py

## Key Points to Note:

1. At most places, I have raised and caught general Exception for simplicity purpose. But in a real system, this should be avoided as it can hide some bugs and make difficult to debug. Instead, specific or custom exceptions should be defined and used.
2. Getters and Setters should be defined for all the attributes in a class. They have been left out here for simplicity.
3. Since this a console based app, I have assumed that only a single user would be using the application at a time.
