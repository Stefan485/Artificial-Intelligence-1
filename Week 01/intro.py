import math

"""
Python is interpreted script language and runs line by line.
This is multiline comment or docstring.
Python uses whitespaces to define scope of code blocks instead of curly braces.
Reserved words: 
    and, as, assert, break, class, continue, def, del, elif, else, except, exec,
    finally, for, from, global, if, import, in, is, lambda, not, or, pass, print,
    raise, return, try, while, with, yield

Data types are dynamic and variables are not declared.
"""

# Numbers
a = 1 # int
b = 2.0 # float
c = 3 + 4j # complex
print(a, b, c)

# Operators on numbers
print("Operators on numbers")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # floor division
print(a % b) # modulo
print(a ** b) # power
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
a += b
print(a)
print("-" * 20)

# Math module
print("Math module")
print(math.pi)
print(math.ceil(math.e))
print(math.sin(math.pi))
print(math.sqrt(a))
print(round(math.log(a, 2), 2))
print("-" * 20)

# Numbers type casting
print("Numbers type casting")
print(int(2.3))
print(float(2))
print(complex(2))
# we can check types of varibles with type() function
print(type(2))
print(type(2.0))
print(type(2 + 3j))
print(type(2 + 3))
print(type(2.0 + 3))
print(type(4 / 2))
print(type(4 // 2))
print("-" * 20)

# Boolean
print("Boolean")
print(True)
print(False)
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(0.0))
print(bool([]))
print(bool([1]))
print(bool(()))
print(bool((1)))
print(bool({}))
print(bool({1}))
print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool(None))
