# Python List: Comprehensive Guide to Functions and Methods

# --- List Methods ---
# Below are commonly used methods available for Python lists with examples:

# 1. append(): Adds an element at the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # Output: [1, 2, 3, 4]

# 2. clear(): Removes all the elements from the list.
my_list.clear()
print("After clear:", my_list)  # Output: []

# 3. copy(): Returns a copy of the list.
my_list = [1, 2, 3]
new_list = my_list.copy()
print("Copy of list:", new_list)  # Output: [1, 2, 3]

# 4. count(): Returns the number of elements with the specified value.
my_list = [1, 2, 3, 2, 2]
print("Count of 2:", my_list.count(2))  # Output: 3

# 5. extend(): Adds elements of an iterable (e.g., list) to the end of the current list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5]

# 6. index(): Returns the index of the first element with the specified value.
print("Index of 3:", my_list.index(3))  # Output: 2

# 7. insert(): Inserts an element at the specified position.
my_list.insert(2, 6)
print("After insert:", my_list)  # Output: [1, 2, 6, 3, 4, 5]

# 8. pop(): Removes and returns the element at the specified position.
removed_item = my_list.pop(2)
print("Removed item:", removed_item)  # Output: 6
print("After pop:", my_list)  # Output: [1, 2, 3, 4, 5]

# 9. remove(): Removes the first occurrence of the specified value.
my_list.remove(3)
print("After remove:", my_list)  # Output: [1, 2, 4, 5]

# 10. reverse(): Reverses the order of the list in place.
my_list.reverse()
print("After reverse:", my_list)  # Output: [5, 4, 2, 1]

# 11. sort(): Sorts the list in ascending order (in place).
my_list.sort()
print("After sort:", my_list)  # Output: [1, 2, 4, 5]

# --- List Functions ---
# These are additional built-in functions that work with lists:

# 12. len(): Returns the number of items in a list.
print("Length of list:", len(my_list))  # Output: 4

# 13. max(): Returns the maximum value in the list.
print("Maximum value:", max(my_list))  # Output: 5

# 14. min(): Returns the minimum value in the list.
print("Minimum value:", min(my_list))  # Output: 1

# 15. sum(): Returns the sum of all elements in the list.
print("Sum of elements:", sum(my_list))  # Output: 12

# 16. sorted(): Returns a sorted list (does not modify the original).
unsorted_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)  # Output: [1, 1, 3, 4, 5, 9]
print("Original list:", unsorted_list)  # Output: [3, 1, 4, 1, 5, 9]

# 17. reversed(): Returns a reversed iterator.
reversed_list = list(reversed(unsorted_list))
print("Reversed list:", reversed_list)  # Output: [9, 5, 1, 4, 1, 3]

# 18. any(): Returns True if any element in the list is True.
bool_list = [0, False, 5, None]
print("Any True values?", any(bool_list))  # Output: True

# 19. all(): Returns True if all elements in the list are True.
print("All True values?", all(bool_list))  # Output: False

# 20. enumerate(): Adds a counter to an iterable.
for index, value in enumerate(["a", "b", "c"]):
    print(f"Index {index}, Value: {value}")
# Output:
# Index 0, Value: a
# Index 1, Value: b
# Index 2, Value: c

# 21. zip(): Combines two or more iterables element-wise.
list1 = ["apple", "banana"]
list2 = ["red", "yellow"]
zipped = list(zip(list1, list2))
print("Zipped list:", zipped)  # Output: [('apple', 'red'), ('banana', 'yellow')]

# --- Nested Lists and Advanced Operations ---
# Lists can contain other lists (nested lists), and their methods apply recursively where necessary.

# Nested list example
nested_list = [1, [2, [3, [4]]]]
print("Nested list:", nested_list)  # Output: [1, [2, [3, [4]]]]

# Accessing elements in a nested list
print("Access nested value:", nested_list[1][1][1][0])  # Output: 4

# --- Practice Exercises ---
# 1. Create a list of numbers and find its length, sum, maximum, and minimum values.
# 2. Reverse and sort the list without modifying the original.
# 3. Use list methods to insert, remove, and pop elements, and demonstrate their effects.

# Save this file and use it to experiment with Python list methods and functions!
