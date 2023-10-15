"""
Conditions and loops
"""

# Conditions
print("Conditions")
num = 5
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

age = 20
message = "You can vote" if age >= 18 else "You cannot vote"
print(message)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 if x % 2 == 0 else x for x in numbers]
print(squared_numbers)
print(20 * "-")

# Range
print("Range")
print(range(10))
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))
print(list(range(10, 0, -1)))
for i in range(6):
    print(i)
for i in range(5, -1, -1):
    print(i)
# Try to avoid using range in for loops, use iteration over list elements instead
print(20 * "-")

# Enumerate
print("Enumerate")
l = ["red", "green", "blue"]
for i, color in enumerate(l):
    print(i, color)

# Zip
print("Zip")
l1 = [1, 2, 3]
l2 = ["red", "green", "blue"]
for num, color in zip(l1, l2):
    print(num, color)

# Loops
print("Loops")
# for loop
for i in range(5):
    print(i)
l = [i for i in range(5)]
print(l)
# create a list of squares of all even numbers from 1 to 10
l = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(l)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
print(20 * "-")

# Nested loops
print("Nested loops")
for i in range(3):
    for j in range(3):
        print(i, j)
print(20 * "-")

# Break and continue
print("Break and continue")
for i in range(10):
    if i == 5:
        break
    print(i)
print("-")
for i in range(10):
    if i == 5:
        continue
    print(i)
print(20 * "-")

