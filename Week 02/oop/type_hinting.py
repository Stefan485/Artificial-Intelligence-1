"""
What is type hinting?

Type hinting in Python is a feature that allows you to specify the expected
data types of variables, function parameters, and return values in your code. 
It provides a way to annotate your code with hints about the types of values 
that variables and functions should handle. Type hints are not enforced by 
the Python interpreter at runtime; they are primarily used for code documentation, 
static analysis by tools like linters, and improved development environments.
"""

from typing import List, Tuple, Dict, Set, Optional

# Integers
x: int = 42

# Floating-Point Numbers
y: float = 3.14

# Strings
name: str = "John"

# Boolean
flag: bool = True

# Lists
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuples
point: Tuple[float, float] = (3.0, 4.0)

# Dictionaries
person: Dict[str, int] = {'age': 30, 'height': 180}

# Sets
fruits: Set[str] = {'apple', 'banana', 'cherry'}

# Custom Classes
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

john: Person = Person("John", 30)

# Optional Types
message: Optional[str] = None

# Function Type Hints
def add(x: int, y: int) -> int:
    return x + y

# Type Hints for Default Arguments
def greet(name: str = "World") -> str:
    return f"Hello, {name}!"
