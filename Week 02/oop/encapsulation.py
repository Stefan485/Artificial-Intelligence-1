"""
What is Encapsulation?
Encapsulation is the process of preventing clients from accessing certain properties, 
which can only be accessed through specific methods.
In python encapsulation is achieved by following some naming conventions.
Access modifiers in python: 
    - private attributes are prefixed with __
    - protected attributes are prefixed with _
    - public attributes are not prefixed with anything
To create a private and protected fields python is using name mangling.
"""

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self._price = price # this is a protected attribute
        self.__discount = 0.10 # this is a private attribute

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self._price * (1-self.__discount)
        return self._price

    def __str__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self._price}"


if __name__ == "__main__":
    book1 = Book('Book 1', 12, 'Author 1', 120)

    print(book1.title)
    print(book1.quantity)
    print(book1.author)
    print(book1.get_price())
    print(book1._Book__discount) # name mangling
    print(book1.__discount) # this will throw an error