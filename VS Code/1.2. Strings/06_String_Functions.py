"""
This file contains Python string functions with explanations and examples.
"""

# 1. capitalize()
# Converts the first character to uppercase
example = "hello"
print(example.capitalize())  # Output: "Hello"

# 2. casefold()
# Converts to lowercase (more aggressive than lower())
example = "ß"
print(example.casefold())  # Output: "ss"

# 3. center()
# Centers the string with padding
example = "hello"
print(example.center(10, '-'))  # Output: "--hello--"

# 4. count()
# Counts occurrences of a substring
example = "banana"
print(example.count("a"))  # Output: 3

# 5. encode()
# Encodes the string into bytes
example = "hello"
print(example.encode("utf-8"))  # Output: b'hello'

# 6. endswith()
# Checks if string ends with a suffix
example = "hello"
print(example.endswith("o"))  # Output: True

# 7. expandtabs()
# Replaces tabs with spaces
example = "hello\tworld"
print(example.expandtabs(4))  # Output: "hello   world"

# 8. find()
# Finds the first occurrence of a substring
example = "hello"
print(example.find("l"))  # Output: 2

# 9. format()
# Formats the string using placeholders
example = "Hello, {}"
print(example.format("World"))  # Output: "Hello, World"

# 10. format_map()
# Formats the string using a mapping
example = "{name}"
mapping = {"name": "Alice"}
print(example.format_map(mapping))  # Output: "Alice"

# 11. index()
# Returns the index of the first occurrence of a substring
example = "hello"
print(example.index("l"))  # Output: 2

# 12. isalnum()
# Checks if all characters are alphanumeric
example = "abc123"
print(example.isalnum())  # Output: True

# 13. isalpha()
# Checks if all characters are alphabetic
example = "abc"
print(example.isalpha())  # Output: True

# 14. isascii()
# Checks if all characters are ASCII
example = "abc"
print(example.isascii())  # Output: True

# 15. isdecimal()
# Checks if all characters are decimal
example = "123"
print(example.isdecimal())  # Output: True

# 16. isdigit()
# Checks if all characters are digits
example = "123"
print(example.isdigit())  # Output: True

# 17. isidentifier()
# Checks if the string is a valid Python identifier
example = "var_1"
print(example.isidentifier())  # Output: True

# 18. islower()
# Checks if all characters are lowercase
example = "hello"
print(example.islower())  # Output: True

# 19. isnumeric()
# Checks if all characters are numeric
example = "123"
print(example.isnumeric())  # Output: True

# 20. isprintable()
# Checks if all characters are printable
example = "hello"
print(example.isprintable())  # Output: True

# 21. isspace()
# Checks if the string contains only whitespace
example = "   "
print(example.isspace())  # Output: True

# 22. istitle()
# Checks if the string is in title case
example = "Hello World"
print(example.istitle())  # Output: True

# 23. isupper()
# Checks if all characters are uppercase
example = "HELLO"
print(example.isupper())  # Output: True

# 24. join()
# Joins elements of an iterable with the string as the separator
example = ","
print(example.join(["a", "b", "c"]))  # Output: "a,b,c"

# 25. ljust()
# Left-justifies the string with padding
example = "hello"
print(example.ljust(10, '-'))  # Output: "hello-----"

# 26. lower()
# Converts the string to lowercase
example = "HELLO"
print(example.lower())  # Output: "hello"

# 27. lstrip()
# Removes leading whitespace or characters
example = "  hello"
print(example.lstrip())  # Output: "hello"

# 28. maketrans()
# Creates a translation table for translate()
trans_table = str.maketrans("abc", "123")
print("abc".translate(trans_table))  # Output: "123"

# 29. partition(
# Splits the string at the first occurrence of the separator
example = "hello world"
print(example.partition(" "))  # Output: ('hello', ' ', 'world')

# 30. replace()
# Replaces occurrences of a substring
example = "hello"
print(example.replace("l", "x"))  # Output: "hexxo"

# 31. rfind()
# Finds the last occurrence of a substring
example = "hello"
print(example.rfind("l"))  # Output: 3

# 32. rindex()
# Like rfind(), but raises ValueError if not found
example = "hello"
print(example.rindex("l"))  # Output: 3

# 33. rjust()
# Right-justifies the string with padding
example = "hello"
print(example.rjust(10, '-'))  # Output: "-----hello"

# 34. rpartition()
# Splits the string at the last occurrence of the separator
example = "hello world"
print(example.rpartition(" "))  # Output: ('hello', ' ', 'world')

# 35. rsplit()
# Splits the string from the right
example = "a,b,c"
print(example.rsplit(",", 1))  # Output: ['a,b', 'c']

# 36. rstrip()
# Removes trailing whitespace or characters
example = "hello   "
print(example.rstrip())  # Output: "hello"

# 37. split()
# Splits the string into a list
example = "a,b,c"
print(example.split(","))  # Output: ['a', 'b', 'c']

# 38. splitlines()
# Splits the string at line breaks
example = "hello\nworld"
print(example.splitlines())  # Output: ['hello', 'world']

# 39. startswith()
# Checks if the string starts with a prefix
example = "hello"
print(example.startswith("he"))  # Output: True

# 40. strip()
# Removes leading and trailing whitespace or characters
example = "  hello  "
print(example.strip())  # Output: "hello"

# 41. swapcase()
# Swaps case of all characters in the string
example = "Hello"
print(example.swapcase())  # Output: "hELLO"

# 42. title()
# Converts the string to title case
example = "hello world"
print(example.title())  # Output: "Hello World"

# 43. translate()
# Translates the string using a translation table
trans_table = str.maketrans("h", "y")
print("hello".translate(trans_table))  # Output: "yello"

# 44. upper()
# Converts the string to uppercase
example = "hello"
print(example.upper())  # Output: "HELLO"

# 45. zfill()
# Pads the string with zeros on the left
example = "42"
print(example.zfill(5))  # Output: "00042"
