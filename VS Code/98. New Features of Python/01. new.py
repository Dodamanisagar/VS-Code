# Newly Added Features in Python (Up to Python 3.11)

# 1. Structural Pattern Matching (Python 3.10)
# A new feature allowing matching against patterns like in switch-case statements in other languages.

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # OK
print(http_status(404))  # Not Found


# 2. Parenthesized Context Managers (Python 3.10)
# Allowing better readability when using multiple context managers.

# Before Python 3.10
# with open('file1.txt') as f1, open('file2.txt') as f2:
#     pass

# With Python 3.10 (Parenthesized)
with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    print("Both files opened successfully!")


# 3. Type Hinting Enhancements (Python 3.10 & 3.11)
# `|` operator for Union types (Python 3.10)

def add(x: int | float, y: int | float) -> int | float:
    return x + y

print(add(3, 5))  # 8
print(add(3.5, 2))  # 5.5


# 4. Precise Error Locations (Python 3.10)
# Python now shows more precise locations for syntax errors.

# Example: Uncomment below code to see the error
# eval("2 +")  # This will now point to the exact location of the syntax error.


# 5. New Features in `str` (Python 3.11)
# Introduced `str.removeprefix()` and `str.removesuffix()` methods for easier string manipulation.

text = "prefix_example_suffix"
print(text.removeprefix("prefix_"))  # example_suffix
print(text.removesuffix("_suffix"))  # prefix_example


# 6. Exception Groups (Python 3.11)
# Handling multiple exceptions together using `ExceptionGroup`.

try:
    raise ExceptionGroup("Multiple Errors", [ValueError("Value error"), TypeError("Type error")])
except ExceptionGroup as eg:
    for ex in eg.exceptions:
        print(f"Caught: {ex}")


# 7. `zoneinfo` Module (Python 3.9)
# Provides support for IANA time zones.

from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2025, 1, 7, tzinfo=ZoneInfo("Asia/Kolkata"))
print(dt)  # 2025-01-07 00:00:00+05:30


# 8. Dictionary Merge and Update Operators (Python 3.9)
# Introduced `|` and `|=` for merging dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2  # Merge dictionaries
print(merged_dict)  # {'a': 1, 'b': 3, 'c': 4}


# 9. Flexible Function and Variable Annotations (Python 3.9)
# Now allows annotations using any valid Python expressions.

from typing import List

a: list[int] = [1, 2, 3]  # Annotation with a valid expression
print(a)


# 10. Performance Improvements (Python 3.11)
# Python 3.11 introduced significant performance improvements, with some operations being 10-60% faster.

# Example: Faster list comprehensions and built-in functions.
large_list = [i for i in range(10**6)]
filtered_list = [x for x in large_list if x % 2 == 0]


# 11. Enhanced Error Messages (Python 3.10 & 3.11)
# Python now provides more helpful error messages for common mistakes.

# Example: Uncomment below to see the error message
# x = [1, 2, 3]
# print(x[5])  # Points to the exact index causing the issue.


# 12. New Syntax: Assignment Expressions (Python 3.8)
# Introduced the "walrus operator" (`:=`) for assignment within expressions.

numbers = [10, 20, 30]
if (n := len(numbers)) > 2:
    print(f"The list has {n} elements.")  # The list has 3 elements.


# 13. Positional-Only Parameters (Python 3.8)
# Allows defining positional-only arguments using `/`.

def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sagar"))  # Hello, Sagar!
# print(greet(name="Sagar"))  # Raises an error because `name` is positional-only.


# 14. F-Strings with Debugging Support (Python 3.8)
# Enhanced f-strings for debugging.

value = 42
print(f"{value=}")  # value=42


# 15. Self-Type Annotations (Python 3.11)
# Enables better type hints for methods returning the instance of the same class.

from typing import Self

class MyClass:
    def my_method(self) -> Self:
        return self

obj = MyClass().my_method()


# 16. Deprecations and Changes
# Deprecated or changed features across recent versions.
# Example: `is` operator should no longer be used for comparing literal values.
# if x is 42:  # Deprecated; use x == 42 instead.

# Summary of Python Versions Covered:
# - Python 3.8: Assignment expressions, positional-only parameters, enhanced f-strings.
# - Python 3.9: Dictionary merge/update operators, zoneinfo module, flexible annotations.
# - Python 3.10: Structural pattern matching, parenthesized context managers, precise errors.
# - Python 3.11: Exception groups, str.removeprefix(), str.removesuffix(), performance improvements, self-type annotations.
