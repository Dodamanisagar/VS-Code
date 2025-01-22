# Tuple Methods in Python

# Tuples have a limited set of built-in methods due to their immutable nature.
# Below are the methods available for tuples with examples:

# --- count() ---
# Returns the number of occurrences of a specified value in the tuple.
example_tuple = (1, 2, 2, 3, 2, 4)
count_of_2 = example_tuple.count(2)
print("Count of 2:", count_of_2)  # Output: 3

# --- index() ---
# Returns the index of the first occurrence of a specified value.
# Raises a ValueError if the value is not found.
index_of_3 = example_tuple.index(3)
print("Index of 3:", index_of_3)  # Output: 3

# --- len() ---
# Not a method, but a built-in function to get the length of a tuple.
length = len(example_tuple)
print("Length of tuple:", length)  # Output: 6

# --- min() and max() ---
# Not methods but built-in functions to get the smallest and largest elements in a tuple.
min_value = min(example_tuple)
max_value = max(example_tuple)
print("Minimum value:", min_value)  # Output: 1
print("Maximum value:", max_value)  # Output: 4

# --- sum() ---
# Not a method but a built-in function to calculate the sum of all elements in a tuple (numeric values only).
sum_of_elements = sum(example_tuple)
print("Sum of elements:", sum_of_elements)  # Output: 14

# --- sorted() ---
# Not a method but a built-in function that returns a sorted list of the tuple elements.
sorted_tuple = sorted(example_tuple)
print("Sorted tuple:", sorted_tuple)  # Output: [1, 2, 2, 2, 3, 4]

# --- any() and all() ---
# any() returns True if at least one element in the tuple is truthy.
# all() returns True if all elements in the tuple are truthy.
example_tuple_2 = (0, 1, 2, 3)
print("Any true values:", any(example_tuple_2))  # Output: True
print("All true values:", all(example_tuple_2))  # Output: False

# --- tuple() ---
# The tuple() function converts an iterable (like a list or string) into a tuple.
example_list = ["a", "b", "c"]
converted_tuple = tuple(example_list)
print("Converted Tuple:", converted_tuple)  # Output: ('a', 'b', 'c')

# --- Example Summary ---
# While tuples have fewer methods than lists, the immutability of tuples makes them ideal for certain use cases where data integrity is critical.
