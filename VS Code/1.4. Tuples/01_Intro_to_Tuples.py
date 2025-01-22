# Comprehensive Notes on Tuples in Python

# --- Introduction to Tuples ---
# A tuple is a collection of ordered elements, similar to a list, but it is immutable.
# Tuples are defined by placing elements inside parentheses `()` separated by commas.

# Characteristics of Tuples:
# 1. Tuples are ordered: Elements maintain their defined order.
# 2. Tuples are immutable: Once defined, elements cannot be added, removed, or changed.
# 3. Tuples allow duplicate elements.
# 4. Tuples can hold elements of mixed data types.

# Example of a Tuple
example_tuple = (1, 2, 3, 4, 5)
print("Tuple:", example_tuple)  # Output: (1, 2, 3, 4, 5)

# --- Creating Tuples ---
# Tuples can be created with or without parentheses (parentheses are optional).

# Example:
tuple1 = ("apple", "banana", "cherry")  # With parentheses
tuple2 = "dog", "cat", "rabbit"  # Without parentheses
print("Tuple1:", tuple1)  # Output: ('apple', 'banana', 'cherry')
print("Tuple2:", tuple2)  # Output: ('dog', 'cat', 'rabbit')

# A single-element tuple requires a trailing comma:
single_element_tuple = ("single",)
print("Single-element tuple:", single_element_tuple)  # Output: ('single',)

# --- Accessing Tuple Elements ---
# Elements can be accessed using their index (0-based).
tuple3 = ("Python", "Java", "C++")
print("First Element:", tuple3[0])  # Output: Python
print("Last Element:", tuple3[-1])  # Output: C++

# --- Slicing Tuples ---
# Use slicing to access a range of elements.
print("Slice:", tuple3[0:2])  # Output: ('Python', 'Java')

# --- Tuple Immutability ---
# Tuples cannot be modified (add, remove, or change elements).
# The following will raise an error:
try:
    tuple3[1] = "C#"  # TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print("Error:", e)

# --- Looping through a Tuple ---
for language in tuple3:
    print("Language:", language)
# Output:
# Language: Python
# Language: Java
# Language: C++

# --- Nested Tuples ---
# Tuples can contain other tuples as elements.
nested_tuple = (1, 2, (3, 4), (5, (6, 7)))
print("Nested Tuple:", nested_tuple)  # Output: (1, 2, (3, 4), (5, (6, 7)))
print("Access Nested Element:", nested_tuple[3][1][0])  # Output: 6

# --- Tuple Unpacking ---
# Tuples can be unpacked into variables.
coordinates = (10, 20, 30)
x, y, z = coordinates
print("X:", x)  # Output: 10
print("Y:", y)  # Output: 20
print("Z:", z)  # Output: 30

# --- Tuple Concatenation and Repetition ---
# Tuples can be concatenated or repeated using + and * operators.
tuple4 = (1, 2, 3)
tuple5 = (4, 5, 6)
concatenated = tuple4 + tuple5
repeated = tuple4 * 2
print("Concatenated Tuple:", concatenated)  # Output: (1, 2, 3, 4, 5, 6)
print("Repeated Tuple:", repeated)  # Output: (1, 2, 3, 1, 2, 3)

# --- Checking Membership ---
# Use 'in' or 'not in' to check if an element exists in a tuple.
tuple6 = ("apple", "banana", "cherry")
print("'apple' in tuple6:", "apple" in tuple6)  # Output: True
print("'grape' not in tuple6:", "grape" not in tuple6)  # Output: True

# --- Practical Applications of Tuples ---
# 1. Tuples are often used for returning multiple values from a function.
# 2. Tuples are used to represent fixed collections of items like coordinates, RGB colors, etc.

def get_point():
    return (10, 20)

point = get_point()
print("Point:", point)  # Output: (10, 20)



# --- Summary ---
# Tuples are a versatile and immutable data structure in Python. They are lightweight and useful for fixed datasets.
# Use tuples when you need an immutable sequence of elements or want to use a collection as a dictionary key.
