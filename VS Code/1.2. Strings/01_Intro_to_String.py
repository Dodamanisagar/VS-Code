# Introduction to Strings in Python

# Strings are one of the most commonly used data types in Python.
# They are used to represent text and are enclosed in quotes.
# You can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) to define a string.
# Triple quotes are often used for multi-line strings or docstrings.
# Strings are immutable, meaning once they are created, they cannot be changed.
# However, you can create new strings based on modifications of existing strings.
# Strings support various operations such as concatenation, repetition, slicing, and indexing.
# Python provides a rich set of built-in methods for string manipulation.
# Strings can also contain Unicode characters, making Python suitable for handling multilingual text.

# Examples of strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello,
World!'''
raw_string = r"This is a raw string where \n is not treated as a newline."

# String Immutability

# Strings in Python are immutable, meaning you cannot change them in place
# However, you can create a new string based on modifications
immutable_string = "Hello"
new_string = immutable_string.replace("H", "J")
print(new_string)  # Output: Jello

# String Concatenation
# Strings can be concatenated using the `+` operator or by using formatted strings.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2 + "!"
print(concatenated_string)  # Output: Hello, World!

# String Repetition
# The `*` operator can be used to repeat strings.
repeated_string = "Ha" * 3
print(repeated_string)  # Output: HaHaHa

# Escape Sequence Characters
# Escape sequences are used to represent certain special characters within strings.
# They are represented by a backslash (\) followed by a character.
# Common escape sequences include:
# \n - Newline
# \t - Tab
# \\ - Backslash
# \' - Single quote
# \" - Double quote

# Examples of escape sequences
newline_string = "Hello,\nWorld!"
tabbed_string = "Hello,\tWorld!"
escaped_backslash_string = "This is a backslash: \\\""
single_quote_string = 'It\'s a beautiful day!'
double_quote_string = "He said, \"Hello, World!\""

print(newline_string)
print(tabbed_string)
print(escaped_backslash_string)
print(single_quote_string)
print(double_quote_string)

# String Slicing and Indexing
# Strings can be indexed and sliced using square brackets [].
# Indexing starts from 0 for the first character and -1 for the last character.
example_string = "Hello, World!"
print(example_string[0])  # Output: H
print(example_string[-1])  # Output: !

# Slicing
# You can use slicing to extract a portion of a string.
sliced_string = example_string[0:5]
print(sliced_string)  # Output: Hello

# String Methods
# Python provides numerous built-in methods for string manipulation, such as:
# .lower(), .upper(), .strip(), .split(), .join(), .replace(), .find(), .startswith(), .endswith(), etc.
example_string = "  Hello, Python!  "
print(example_string.lower())  # Output:   hello, python!  
print(example_string.upper())  # Output:   HELLO, PYTHON!  
print(example_string.strip())  # Output: Hello, Python!
print(example_string.split())  # Output: ['Hello,', 'Python!']
print("-".join(["Python", "is", "fun"]))  # Output: Python-is-fun
print(example_string.find("Python"))  # Output: 9

# Formatted Strings (f-strings)
# Introduced in Python 3.6, f-strings allow embedding expressions inside string literals.
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

# Multi-line Strings
# Triple quotes are often used for multi-line strings or for documentation (docstrings).
long_string = """This is an example of
a multi-line string."""
print(long_string)

# Raw Strings
# Raw strings are useful when dealing with regular expressions or file paths.
raw_string = r"C:\\Users\\Name"
print(raw_string)  # Output: C:\Users\Name

# Unicode Strings
# Python strings support Unicode, allowing them to handle text in multiple languages.
unicode_string = "こんにちは"  # Japanese for "Hello"
print(unicode_string)

# String Length
# Use the `len()` function to determine the length of a string.
print(len(example_string))  # Output: 18

# Practice Examples
# Practice 1: Reverse a string
reversed_string = example_string[::-1]
print(reversed_string)  # Output: !nohtyP ,olleH

# Practice 2: Check if a string is a palindrome
palindrome_candidate = "madam"
is_palindrome = palindrome_candidate == palindrome_candidate[::-1]
print(is_palindrome)  # Output: True
