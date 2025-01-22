# Python Lists: Comprehensive Guide

# --- Introduction to Lists ---
# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. 
# Each element or value that is inside of a list is called an item. 
# Lists are defined by having values between square brackets [ ].

# Example:
example_list = [1, 2, 3, 4, 5]
print(example_list)  # Output: [1, 2, 3, 4, 5]

# Lists can contain items of different types:
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)  # Output: [1, 'Hello', 3.14, True]

# Lists are ordered, meaning that the items have a defined order, and that order will not change unless we explicitly do so.
# Lists are changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing items in a list
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Changing the value of a list item
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Looping through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# blueberry
# cherry

# Checking if an item is in the list
if "apple" in fruits:
    print("Apple is in the list")

# Nested lists
nested_list = [1, 2, [3, 4], [5, [6, 7]]]
print(nested_list)  # Output: [1, 2, [3, 4], [5, [6, 7]]]
print(nested_list[2])  # Output: [3, 4]
print(nested_list[3][1])  # Output: [6, 7]
print(nested_list[3][1][0])  # Output: 6

# --- Basic Concepts ---
# Lists are one of the most versatile data structures in Python. They are used to store multiple items in a single variable.
# Characteristics of Lists:
# 1. Ordered: The order of elements is preserved.
# 2. Mutable: You can change, add, or remove elements after creation.
# 3. Allow Duplicates: Lists can contain duplicate elements.
# 4. Heterogeneous: Lists can store elements of different data types.

# Example of creating a list:
basic_list = [1, 2, 3, 4, 5]
print("Basic List:", basic_list)

# Lists can also store strings, booleans, or even other lists:
mixed_list = ["apple", 3.14, True, [1, 2, 3]]
print("Mixed List:", mixed_list)

# --- Accessing Elements in a List ---
# Elements are accessed using their index (starting from 0).
example_list = [10, 20, 30, 40, 50]
print("First Element:", example_list[0])
print("Last Element:", example_list[-1])  # Negative indexing starts from the end

# --- Modifying a List ---
# Change an element by assigning a new value.
example_list[1] = 25
print("Modified List:", example_list)

# --- Adding Elements to a List ---
# Use append() to add a single element at the end.
example_list.append(60)
print("After Append:", example_list)

# Use extend() to add multiple elements at the end.
example_list.extend([70, 80])
print("After Extend:", example_list)

# Use insert() to add an element at a specific index.
example_list.insert(2, 99)
print("After Insert:", example_list)

# --- Removing Elements from a List ---
# Use remove() to delete a specific element by value.
example_list.remove(30)  # Removes the first occurrence of 30
print("After Remove:", example_list)

# Use pop() to remove an element by index (and return it).
popped_element = example_list.pop(3)
print("Popped Element:", popped_element)
print("After Pop:", example_list)

# Use del to remove an element by index or slice.
del example_list[0]
print("After Del:", example_list)

# Use clear() to empty the list.
example_list.clear()
print("After Clear:", example_list)

# --- Advanced Operations ---
# 1. Slicing: Extract a sub-list.
slicing_example = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slice [2:5]:", slicing_example[2:5])  # Elements from index 2 to 4
print("Slice [:4]:", slicing_example[:4])   # Elements from start to index 3
print("Slice [5:]:", slicing_example[5:])   # Elements from index 5 to the end

# 2. List Comprehension: Create lists using a concise syntax.
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# 3. Sorting and Reversing Lists:
sorting_example = [5, 2, 9, 1, 5, 6]
sorting_example.sort()  # Sorts in ascending order
print("Sorted List:", sorting_example)

sorting_example.sort(reverse=True)  # Sorts in descending order
print("Reverse Sorted List:", sorting_example)

sorting_example.reverse()  # Reverses the order of elements
print("Reversed List:", sorting_example)

# 4. Copying Lists:
original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Copied List:", copied_list)

# 5. Nested Lists:
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested_list)
print("Access Nested Element:", nested_list[1][0])  # Accessing element 3

# --- Common List Methods ---
# count(): Counts the occurrences of a specific element.
count_example = [1, 2, 3, 1, 1, 4]
print("Count of 1:", count_example.count(1))

# index(): Finds the first occurrence of a value.
print("Index of 3:", count_example.index(3))

# len(): Returns the number of elements in the list.
print("Length of List:", len(count_example))

# --- Practice Exercise ---
# Task: Create a list of your favorite fruits and perform the following:
# 1. Add two more fruits to the list.
# 2. Remove one fruit by value.
# 3. Sort the list alphabetically.
# 4. Reverse the order of the sorted list.

# Solution:
favorite_fruits = ["apple", "banana", "cherry"]
favorite_fruits.append("mango")
favorite_fruits.append("orange")
print("After Adding Fruits:", favorite_fruits)

favorite_fruits.remove("banana")
print("After Removing 'banana':", favorite_fruits)

favorite_fruits.sort()
print("Sorted Fruits:", favorite_fruits)

favorite_fruits.reverse()
print("Reversed Sorted Fruits:", favorite_fruits)

# Save and run this file to understand and practice list operations.
