"""
What are Static Methods?

Static methods are methods that are bound to a class rather than its object.
Static fields are fields that are bound to a class rather than its object.

We will extend our example with books, so that we use static methods and fields.
"""

class Book:
    total_books_sold = 0 # this is a private attribute

    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self._price = price # this is a protected attribute
        self.__discount = 0.10 # this is a private attribute
        Book.total_books_sold += quantity

    @staticmethod
    def equals(book1, book2):
        return book1.title == book2.title and book1.author == book2.author

    def set_discount(self, discount):
        Book.__discount = discount

    def get_price(self):
        if Book.__discount:
            return self.__price * (1-Book.__discount)
        return self.__price

    def __str__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.__price}"
    
if __name__ == "__main__":
    book1 = Book('Book 1', 12, 'Author 1', 120)
    book2 = Book('Book 2', 18, 'Author 2', 220)

    print(Book.equals(book1, book2))
    print(f"Number of total sold books: {Book.total_books_sold}")