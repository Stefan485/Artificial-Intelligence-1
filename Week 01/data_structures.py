from collections import deque
from queue import PriorityQueue
import heapq
"""
Some of data structures in Python that we will use in this course are:
list - mutable sequence of objects
tuple - immutable sequence of objects
set - mutable unordered collection of unique objects (equivalent of hash set in Java)
dict - mutable unordered collection of key-value pairs (equivalent of hash map in Java)
deque - mutable sequence of objects with fast appends and pops on either end
priority queue - mutable sequence of objects sorted by key
"""

# LISTS
print("LISTS")
# Example 1: Creating an empty list
# Time Complexity: O(1) - Constant time.
empty_list = []
print("Empty List:", empty_list)

# Example 2: Creating a list with elements
# Time Complexity: O(n) - Linear time, where n is the number of elements.
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Example 3: Accessing list elements by index
# Time Complexity: O(1) - Constant time.
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Example 4: Modifying list elements
# Time Complexity: O(1) - Constant time (for a specific index).
fruits[1] = "orange"
print("Updated Fruits List:", fruits)

# Example 5: Appending an element to the end of the list
# Time Complexity: O(1) - Constant time.
fruits.append("grape")
print("Fruits List with Grape:", fruits)

# Example 6: Inserting an element at a specific index
# Time Complexity: O(n) - Linear time (in the worst case when inserting at the beginning).
fruits.insert(1, "kiwi")
print("Fruits List with Kiwi:", fruits)

# Example 7: Removing an element by value
# Time Complexity: O(n) - Linear time (in the worst case when removing the first occurrence).
fruits.remove("cherry")
print("Fruits List without Cherry:", fruits)

# Example 8: Removing an element by index
# Time Complexity: O(n) - Linear time (in the worst case when removing from the beginning).
popped_fruit = fruits.pop(2)
print("Popped Fruit:", popped_fruit)
print("Fruits List after Pop:", fruits)

# Example 9: Checking if an element exists in the list
# Time Complexity: O(n) - Linear time (in the worst case when checking the last element).
if "apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# Example 10: Finding the index of an element
# Time Complexity: O(n) - Linear time (in the worst case when searching at the end).
index = fruits.index("kiwi")
print("Index of Kiwi:", index)

# Example 11: Sorting a list
# Time Complexity: O(n*log(n)) - Average time for a comparison sort (e.g., Timsort).
fruits.sort()
print("Sorted Fruits List:", fruits)

# Example 12: Reversing a list
# Time Complexity: O(n) - Linear time, as it iterates through the entire list.
fruits.reverse()
print("Reversed Fruits List:", fruits)

# Example 13: Finding the length of the list
# Time Complexity: O(1) - Constant time.
length = len(fruits)
print("Number of Fruits:", length)

# Example 14: Slicing a list
# Time Complexity: O(k) - Slicing a list from index i to j takes O(j - i) time.
slice = fruits[1:3]
print("Sliced Fruits:", slice)

# Example 15: Copying a list (shallow copy)
# Time Complexity: O(n) - Linear time, as it copies each element to the new list.
fruits_copy = fruits.copy()
print("Copied Fruits List:", fruits_copy)

# Exampele 16: Lists does not need to be homogeneous
mixed_list = ["Alice", 1, True]
print("Mixed List:", mixed_list)

print("--------------------------------------------------------------------------------")

# TUPLES
print("TUPLES")
# Example 1: Creating an empty tuple
# Time Complexity: O(1) - Constant time.
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Example 2: Creating a tuple with elements
# Time Complexity: O(n) - Linear time, where n is the number of elements.
fruits = ("apple", "banana", "cherry")
print("Fruits Tuple:", fruits)

# Example 3: Accessing tuple elements by index
# Time Complexity: O(1) - Constant time.
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Example 4: Creating a list of tuples
student_grades = [
    ("Alice", "Smith", 95),
    ("Bob", "Johnson", 88),
    ("Eve", "Davis", 92),
]

# Example 5: Iterating over the list of tuples
for student in student_grades:
    first_name, last_name, grade = student
    print(f"{first_name} {last_name} scored {grade} points.")

# Example 6: Filtering based on a condition
high_achievers = [student for student in student_grades if student[2] >= 90]
print("High Achievers:", high_achievers)

# Example 7: Sorting the list of tuples by a specific key
sorted_grades = sorted(student_grades, key=lambda x: x[2], reverse=True)
print("Sorted by Grade (High to Low):", sorted_grades)

# Example 8 - Tuple does not need to be homogeneous
mixed_tuple = ("Alice", 1, True)
print("Mixed Tuple:", mixed_tuple)

print("--------------------------------------------------------------------------------")

# SETS
print("SETS")
# Example 1: Creating a set
# Time Complexity: O(n) - Constant time.
fruits = {"apple", "banana", "cherry"}
print("Fruits Set:", fruits)

# Example 2: Adding elements to a set
# Time Complexity: O(1) - Constant time.
fruits.add("orange")
print("Fruits Set with Orange:", fruits)

# Example 3: Removing elements from a set
# Time Complexity: O(1) - Constant time.
fruits.remove("cherry")
print("Fruits Set without Cherry:", fruits)

# Example 4: Checking if an element is in the set
# Time Complexity: O(1) - Constant time.
if "apple" in fruits:
    print("Apple is in the set.")
else:
    print("Apple is not in the set.")

# Example 5: Set operations (union, intersection, difference)
# Time Complexity: O(len(s)) - Linear time, where 's' is the larger set for union, intersection, and difference.
other_fruits = {"banana", "kiwi", "strawberry"}
union_result = fruits | other_fruits  # Union
intersection_result = fruits & other_fruits  # Intersection
difference_result = fruits - other_fruits  # Difference
print("Union Result:", union_result)
print("Intersection Result:", intersection_result)
print("Difference Result:", difference_result)

# Example 6: Removing an element safely with discard
# Time Complexity: O(1) - Constant time.
fruits.discard("grape")  # No error if "grape" is not in the set
print("Fruits Set with Discard:", fruits)

# Example 7: Checking if a set is a subset or superset
# Time Complexity: O(len(set2)) - Linear time, where 'set2' is the other set.
subset_check = {"banana", "kiwi"}.issubset(fruits)
superset_check = fruits.issuperset({"banana", "kiwi"})
print("Is {'banana', 'kiwi'} a subset?", subset_check)
print("Is the set a superset of {'banana', 'kiwi'}?", superset_check)

# Example 10: Removing and returning an element
# Time Complexity: O(1) - Constant time.
popped_fruit = fruits.pop()
print("Popped Fruit:", popped_fruit)

# Example 11 - Set does not need to be homogeneous
mixed_set = {"Alice", 1, True}
print("Mixed Set:", mixed_set)

# Example 12: Set comprehensions
# Time Complexity: O(n) - Linear time, where 'n' is the range size.
squared_numbers = {x**2 for x in range(1, 6)}
print("Set Comprehension - Squared Numbers:", squared_numbers)

print("--------------------------------------------------------------------------------")

# DICTIONARIES
print("DICTIONARIES")
# Example 1: Creating a dictionary
# Time Complexity: O(n) - Linear time, where n is the number of elements.
student_grades = {"Alice": 95, "Bob": 88, "Eve": 92}
print("Student Grades:", student_grades)

# Example 2: Adding elements to a dictionary
# Time Complexity: O(1) - Constant time.
student_grades["Charlie"] = 89
print("Student Grades with Charlie:", student_grades)

# Example 3: Modifying elements in a dictionary
# Time Complexity: O(1) - Constant time.
student_grades["Bob"] = 90
print("Updated Student Grades for Bob:", student_grades)

# Example 4: Accessing elements by key
# Time Complexity: O(1) - Constant time.
alice_grade = student_grades["Alice"]
print("Alice's Grade:", alice_grade)

# Example 5: Checking if a key exists in the dictionary
# Time Complexity: O(1) - Constant time.
if "Eve" in student_grades:
    print("Eve's Grade:", student_grades["Eve"])
else:
    print("Eve is not in the dictionary.")

# Example 6: Removing elements from a dictionary
# Time Complexity: O(1) - Constant time.
student_grades.pop("Charlie", None)
print("Student Grades without Charlie:", student_grades)

# Example 7: Iterating over dictionary keys, values, and items
# Time Complexity: O(n) - Linear time, where 'n' is the number of key-value pairs.
print("Keys:", student_grades.keys())
print("Values:", student_grades.values())
print("Items:", student_grades.items())
for student, grade in student_grades.items():
    print(f"{student} scored {grade} points.")

# Example 8 - Dictionary does not need to be homogeneous
my_dict = {
    "name": "John",
    42: "Answer to the Ultimate Question of Life, the Universe, and Everything",
    (1, 2): "A tuple key",
    3.14: "Approximation of Pi"
}
print("My Dictionary:", my_dict)

# Example 9 - Dictionary comprehensions
# Time Complexity: O(n) - Linear time, where 'n' is the range size.
squared_numbers = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension - Squared Numbers:", squared_numbers)

# Bonus
# From Python 3.7 onwards, dictionaries are ordered by insertion order.
# This means that the order of iteration is guaranteed to be the same as the order of insertion.
fruits_prices = {}
fruits_prices["banana"] = 0.99
fruits_prices["cherry"] = 2.99
fruits_prices["apple"] = 1.99
print("Fruits Prices:", fruits_prices)

print("--------------------------------------------------------------------------------")

# DEQUES
print("DEQUES")

# Example 1: Creating a deque
# Time Complexity: O(n) - Linear time, where n is the number of elements.
queue = deque([1, 2, 3, 4, 5])
print("Queue:", queue)

# Example 2: Appending elements to the end of the deque
# Time Complexity: O(1) - Constant time.
queue.append(6)
print("Queue after Append:", queue)

# Example 3: Popping elements from the end of the deque
# Time Complexity: O(1) - Constant time.
popped_end = queue.pop()
print("Popped from End:", popped_end)
print("Queue after Pop from End:", queue)

# Example 4: Appending elements to the beginning of the deque
# Time Complexity: O(1) - Constant time.
queue.appendleft(0)
print("Queue after Append Left:", queue)

# Example 5: Popping elements from the beginning of the deque
# Time Complexity: O(1) - Constant time.
popped_start = queue.popleft()
print("Popped from Start:", popped_start)
print("Queue after Pop from Start:", queue)

# Example 6: Checking if an element exists in the deque
# Time Complexity: O(n) - Linear time.
if 3 in queue:
    print("3 is in the deque.")
else:
    print("3 is not in the deque.")

print("--------------------------------------------------------------------------------")

# PRIORITY QUEUES
print("PRIORITY QUEUES")

# Example 1: Creating a priority queue
# Time Complexity: O(n) - Linear time, where n is the number of elements.
pq = [(3, "apple"), (1, "banana"), (2, "cherry")]
heapq.heapify(pq) 
print("Priority Queue:", pq)

# Example 2: Adding elements to the priority queue
# Time Complexity: O(log n) - Logarithmic time.
heapq.heappush(pq, (4, "grape"))
print("Priority Queue after Adding Elements:", pq)

# Example 3: Peeking at the top element
# Time Complexity: O(1) - Constant time.
top_element = pq[0]  # The smallest element is at index 0
print("Top Element:", top_element)

# Example 4: Removing the top element
# Time Complexity: O(log n) - Logarithmic time.
popped_element = heapq.heappop(pq)  # Removes and returns the smallest element
print("Popped Element:", popped_element)

# Example 5: Checking if the priority queue is empty
# Time Complexity: O(1) - Constant time.
is_empty = not bool(pq)  # Check if the list is empty
print("Is Priority Queue Empty?", is_empty)

