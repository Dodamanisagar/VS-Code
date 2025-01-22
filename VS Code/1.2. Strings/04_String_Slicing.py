# String Slicing

# You can extract a substring from a string using slicing
example_string = "Hello, World!"
substring = example_string[0:5]
print(substring)  # Output: Hello

# More Examples of String Slicing
# Slicing with start and end indices
substring1 = example_string[7:12]
print(substring1)  # Output: World

# Slicing with only start index (goes till the end of the string)
substring2 = example_string[7:]
print(substring2)  # Output: World!

# Slicing with only end index (starts from the beginning of the string)
substring3 = example_string[:5]
print(substring3)  # Output: Hello

# Slicing with negative indices
substring4 = example_string[-6:-1]
print(substring4)  # Output: World

# Slicing with step
substring5 = example_string[::2]
print(substring5)  # Output: Hlo ol!

# Reversing a string using slicing
reversed_string = example_string[::-1]
print(reversed_string)  # Output: !dlroW ,olleH