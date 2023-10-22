"""
What are Classes and Objects?
Python, like every other object-oriented language, allows you to 
define classes to create objects. 
In-built Python classes are the most common data types in Python, 
such as strings, lists, dictionaries, and so on.

A class is a collection of instance variables and related methods 
that define a particular object type. 
You can think of a class as an object's blueprint or template. 
Attributes are the names given to the variables that make up a class.

A class instance with a defined set of properties is called an object. As a result, 
the same class can be used to construct as many objects as needed.

The following is an example of a class definition in Python:
"""

class Book:
    # this is a constructor of the class
    def __init__(self, title, quantity, author, price):
        # definitions of the properties of the class
        # self is a reference to the current instance of the class (equivalent to this in Java)
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    # toString method in python
    # all classes implicitly inherit from object class, 
    # so we can override its __str__ method
    def __str__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


if __name__ == "__main__":
    book1 = Book('Book 1', 12, 'Author 1', 120)
    book2 = Book('Book 2', 18, 'Author 2', 220)
    book3 = Book('Book 3', 28, 'Author 3', 320)
    print(book1)
    print(book2)
    print(book3)