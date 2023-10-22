"""
What is Inheritance?
Inheritance is regarded as the most significant characteristics of OOP.
A class's ability to inherit methods and/or characteristics from another class is known as inheritance.

The subclass or child class is the class that inherits. The superclass or parent class 
is the class from which methods and/or attributes are inherited.

Two new classes have been added to our bookseller's sales software: a Novel class and Academic class.

We can see that regardless of whether a book is classified as novel or academic, 
it may have some similar attributes like title and author, as well as common methods like 
get_price() and set_discount(). Rewriting all that code for each new class is a waste of time, 
effort, and memory.

What is Polymorphism?
Polymorphism refers to a subclass's ability to adapt a method that already exists in its 
superclass to meet its needs. To put it another way, a subclass can use a method from its 
superclass as is or modify it as needed.
"""

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __str__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __str__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


if __name__ == "__main__":
    novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
    novel1.set_discount(0.20)

    academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

    print(novel1)
    print(academic1)