import math

# example of a simpel function that return a value with docstring
def add(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    return a + b

# example of a function that does not return a value with a default parameter
def greet(name, greeting="Hello"):
    """
    Greets a person with a default greeting.

    Args:
        name (str): Name of the person.
        greeting (str): Greeting message (default is "Hello").

    Returns:
        None
    """
    print(f"{greeting}, {name}!")

def calculate_circle_properties(radius):
    """
    Calculate properties of a circle and return its area and circumference.

    Args:
        radius (float): The radius of the circle.

    Returns:
        Tuple (float, float): A tuple containing the area and circumference of the circle.
    """
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


# functions - change of parameters
# in python all parameters are passed by reference
# for immutable parameters (int, float, string, tuple) the change is not visible outside the function
def addInterest(balance, rate):
    newBalance=balance*(1+rate)
    balance=newBalance

def test():
    amount=1000
    rate=0.05
    addInterest(amount,rate)
    print(amount)

# for mutable parameters (list, dictionary) the change is visible outside the function
def add_to_list(list, element):
    list.append(element)

def test2():
    list = [1,2,3]
    add_to_list(list, 4)
    print(list)

# function with variable number of arguments
def test_args(f_arg, *args):
    print("First normal argument f_arg:", f_arg)
    for arg in args:
        print("rest of arguments from *args:", arg)

# function with variable number of keyword arguments
def test_kwargs(f_arg, *args, **kwargs):
    print("First normal argument f_arg:", f_arg)
    for arg in args:
        print("Rest of arguments from *args: ", arg)
    for key in kwargs:
        print(f"Keyword argument: {key}, {kwargs[key]}")

if __name__ == "__main__":
    result = add(3, 4)  # Calling the function and storing the result in 'result'
    print("Sum:", result)  # Prints "Sum: 7"

    # Example of calling the function with and without providing the 'greeting' parameter:
    greet("Alice")          # Uses default greeting: "Hello, Alice!"
    greet("Bob", "Hi")      # Overrides the default: "Hi, Bob!"

    # Example of calling the function and capturing both values in a tuple:
    circle_radius = 5.0
    circle_area, circle_circumference = calculate_circle_properties(circle_radius)
    print(f"Circle Area: {circle_area}, Circumference: {circle_circumference}")

    test()
    test2()
    test_args("Hello", "World", "Python", "Programming")
    test_kwargs("Hello", "World", "Python", "Programming", name="Alice", age=20)

    # Lambda functions
    print("Lambda functions")
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2))

    def f(n):
        return lambda a : a * n
    
    mydoubler = f(2)
    print(mydoubler(11))
    mytripler = f(3)
    print(mytripler(11))

    # Map function
    print("Map function")
    def fahrenheit(T):
        return ((float(9)/5)*T + 32)
    temperatures = (36.5, 37, 37.5, 38, 39)
    print(list(map(fahrenheit, temperatures)))

    # Filter function
    print("Filter function")
    grade_points = [20, 60, 63, 51, 43, 87, 74, 65, 95, 30]
    print(f"Passing grades: {list(filter(lambda x: x >= 50, grade_points))}")