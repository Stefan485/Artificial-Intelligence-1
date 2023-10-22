"""
What are Magic Methods?

Python magic methods, also known as dunder methods (short for "double underscore"), 
are special methods with double underscores at the beginning and end of their names. 
These methods have predefined purposes and are automatically called by Python in 
specific situations, such as object creation, operator overloading, and customizing 
object behavior. Magic methods are used to implement operator overloading, context managers, 
and other special behaviors for custom classes.

Here are some commonly used magic methods in Python:

__init__(self, ...): The constructor method is used to initialize an object when it's created. It is called automatically when you create an instance of a class.

__str__(self): The string representation method is used to return a human-readable string representation of an object when you use str(obj) or print(obj).

__repr__(self): The official string representation method is used to return an unambiguous representation of an object. It is called when you use repr(obj).

__len__(self): The length method is used to define the behavior of the built-in len() function when applied to an object of the class.

__getitem__(self, key): This method allows you to use the indexing operator (e.g., obj[key]) for objects of your class.

__setitem__(self, key, value): This method defines how to set values using the indexing operator (e.g., obj[key] = value).

__delitem__(self, key): This method defines the behavior when you use the del statement to remove items (e.g., del obj[key]).

__iter__(self): The iterator method allows you to define custom iteration behavior for objects of your class.

__next__(self): This method is used to specify what should happen when you call next() on an iterator object created with __iter__.

__enter__(self), __exit__(self, exc_type, exc_value, traceback): These methods are used to implement context managers, allowing you to manage resources and exceptions with the with statement.

__eq__(self, other), __ne__(self, other), __lt__(self, other), etc.: These methods are used to define custom behavior for object comparison and are triggered when using comparison operators (e.g., ==, !=, <, >).

__hash__(self): This method is used to define the behavior of the built-in hash() function when applied to an object of the class.

__add__(self, other), __sub__(self, other), etc.: These methods allow you to overload arithmetic operations (e.g., +, -) for objects of your class.

__call__(self, ...): This method allows you to make an instance of a class callable as if it were a function.

These are just a subset of the many magic methods available in Python. By implementing these methods in your custom classes, you can customize their behavior and take full advantage of Python's object-oriented features. Magic methods are a powerful tool for creating more expressive and intuitive classes in Python.
"""

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imaginary)}i"
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, 
                             self.real * other.imaginary + self.imaginary * other.real)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    
if __name__ == "__main__":
    a = ComplexNumber(2, 3)
    b = ComplexNumber(4, 5)

    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a == b)