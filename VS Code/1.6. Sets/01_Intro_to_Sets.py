# 01_Intro_to_Sets.py

# Introduction to Sets in Python

# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements from them.
# Sets are defined using curly braces {} or the set() function.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding an element:", my_set)

# Adding multiple elements using update()
my_set.update([7, 8, 9])
print("Set after adding multiple elements:", my_set)

# Removing elements from a set
my_set.remove(9)  # Raises KeyError if the element is not found
print("Set after removing an element:", my_set)

# Removing an element using discard()
my_set.discard(8)  # Does not raise an error if the element is not found
print("Set after discarding an element:", my_set)

# Removing an element using pop()
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# Clearing all elements from a set
my_set.clear()
print("Set after clearing all elements:", my_set)

# Set operations

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Checking subset and superset
set3 = {1, 2}
print("set3 is subset of set1:", set3.issubset(set1))
print("set1 is superset of set3:", set1.issuperset(set3))

# Checking for disjoint sets
set4 = {6, 7}
print("set1 and set4 are disjoint:", set1.isdisjoint(set4))

# Set comprehensions
set_comp = {x * x for x in range(1, 6)}
print("Set comprehension:", set_comp)