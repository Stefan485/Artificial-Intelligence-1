
"""
Beside primitive types (which are all objects in Python) there are also collections.
str - immutable sequence of characters (char does not exist in Python)
range - immutable sequence of numbers
list - mutable sequence of objects
tuple - immutable sequence of objects
set - mutable unordered collection of unique objects
dict - mutable unordered collection of key-value pairs
"""

# Strings
print("Strings")
s = "Hello World!"
print(s)
print("Length: ", len(s))
print("Length: " + str(len(s)))
print("First character in string: " + s[0])
print("Last character in string: " + s[-1])
colors = ";".join(["red", "green", "blue"])
print(colors)
print(colors.split(";"))
r, g, b = colors.split(";")
print(r, g, b)
print(3 * "abc")
my_string = input("Enter some string: ")
print("You entered: " + my_string)
print(20 * "-")

# String Slicing
print("String Slicing")
s = "Hello World!"
print(s[0:5])
print(s[6:])
print(s[:5])
print(s[-6:])
print(s[::2]) # 2 specifies step
print(s[::-1]) # reverse string

# String Iteration
print("String Iteration")
for c in s:
    print(c)

# F strings
print("F strings")
name = "John"
age = 20
print(f"Hello {name}, you are {age} years old.")

# String methods
print("String methods")
s = "Hello World!"
print(s)
print(f"Lowercase: {s.upper()}")
print(f"Uppercase: {s.lower()}")
# find returns index of first occurence of substring
print(f"Index of 'o': {s.find('o')}")
# strip removes leading and trailing whitespaces
s += " "
print(f"Strip: {s.strip()}")
# split splits string into list of substrings
print(f"Split: {s.split(' ')}")
# replace replaces all occurences of substring with another substring
print(f"Replace: {s.replace('World', 'Python')}")

