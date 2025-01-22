# String Concatenation in Python

# 1. Using the + operator
# You can concatenate strings using the + operator.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2 + "!"
print("Using + operator:", concatenated_string)
# Output: Hello, World!

# 2. Using join() method
# The join() method joins a sequence of strings together with a specified separator.
strings = ["Hello", "World"]
concatenated_string_join = ", ".join(strings) + "!"
print("Using join() method:", concatenated_string_join)
# Output: Hello, World!

# 3. Using f-strings (formatted string literals)
# F-strings are a concise and readable way to concatenate strings, available in Python 3.6+.
concatenated_string_fstring = f"{string1}, {string2}!"
print("Using f-strings:", concatenated_string_fstring)
# Output: Hello, World!

# 4. Using % formatting (older style)
# The % operator allows string formatting with placeholders, but it is considered outdated.
concatenated_string_percent = "%s, %s!" % (string1, string2)
print("Using % formatting:", concatenated_string_percent)
# Output: Hello, World!

# 5. Using format() method
# The format() method allows inserting variables into strings.
concatenated_string_format = "{}, {}!".format(string1, string2)
print("Using format() method:", concatenated_string_format)
# Output: Hello, World!

# 6. Concatenating with numbers (type conversion)
# You can also concatenate strings with numbers by converting the number to a string using str().
number = 2025
concatenated_string_number = string1 + " " + str(number)
print("Concatenating with numbers:", concatenated_string_number)
# Output: Hello 2025

# 7. Efficiency of different methods
# When concatenating many strings, the join() method is more efficient than using the + operator.
large_list = ["This", "is", "an", "efficient", "method"]
efficient_concatenation = " ".join(large_list)
print("Efficient concatenation using join():", efficient_concatenation)
# Output: This is an efficient method

# Summary:
# 1. + operator: simple but can be inefficient for many strings.
# 2. join() method: most efficient for concatenating many strings.
# 3. f-strings: concise and readable, available in Python 3.6+.
# 4. % formatting: older style, less readable than other methods.
# 5. format() method: flexible and versatile.
