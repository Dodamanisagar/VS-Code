# String Indexing in Python

# You can access individual characters in a string using indexing
example_string = "Hello, World!"

# 1. Accessing the first character (index 0)
first_character = example_string[0]
print("First character:", first_character)
# Output: H

# 2. Accessing the last character using a positive index (index -1)
last_character = example_string[-1]
print("Last character:", last_character)
# Output: !

# 3. Accessing a character using a positive index (index 7)
character_at_index_7 = example_string[7]
print("Character at index 7:", character_at_index_7)
# Output: W

# 4. Accessing a character using a negative index (index -6)
character_at_index_minus_6 = example_string[-6]
print("Character at index -6:", character_at_index_minus_6)
# Output: W

# 5. Demonstrating indexing with a string containing special characters
special_string = "Python 3.9!"
character_at_index_5 = special_string[5]
print("Character at index 5:", character_at_index_5)
# Output: 3

# 6. Attempting to access an index out of range (will raise an IndexError)
try:
    invalid_index = example_string[20]  # Index out of range
except IndexError as e:
    print("Error:", e)
# Output: Error: string index out of range

# Summary:
# 1. Positive indices: Start from 0 for the first character and increment to the right.
# 2. Negative indices: Start from -1 for the last character and decrement to the left.
# 3. Attempting to access an out-of-range index raises an IndexError.
