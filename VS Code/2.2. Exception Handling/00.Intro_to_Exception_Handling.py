# Exception Handling in Python: Concepts, Syntax, and Examples

# 1. What is Exception Handling?
# Exception handling is a mechanism in Python to handle runtime errors and maintain the normal flow of a program.
# Common exceptions: ZeroDivisionError, FileNotFoundError, ValueError, etc.

# Syntax:
# try:
#     # Code that may raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code that runs if no exception occurs
# finally:
#     # Code that always runs, regardless of exceptions


# 2. Example of Exception Handling
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide a number by zero.")
finally:
    print("This block executes no matter what.")
 
# 3. Catching Multiple Exceptions
# Python allows catching multiple exceptions in a single `except` block or separately.

# Example 1: Multiple `except` blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Example 2: Single `except` block for multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")


# 4. Using the `else` Block
# The `else` block executes if no exception occurs in the `try` block.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"The result is {result}")


# 5. Using the `finally` Block
# The `finally` block executes regardless of whether an exception occurs or not.
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("End of file handling process.")


# 6. Raising Exceptions
# You can raise exceptions intentionally using the `raise` keyword.

# Example: Raising an exception
try:
    num = -1
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
except ValueError as e:
    print(e)


# 7. Custom Exceptions
# You can define custom exceptions by creating a new exception class that inherits from `Exception`.

# Example: Custom Exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

try:
    number = -5
    if number < 0:
        raise NegativeNumberError("This is a negative number!")
except NegativeNumberError as e:
    print(e)


# 8. Handling Nested Exceptions
# Python allows nested `try-except` blocks to handle different levels of exceptions.

try:
    try:
        num = 10 / 0
    except ZeroDivisionError:
        print("Inner exception: Division by zero.")
        raise  # Re-raise the exception to the outer block
except ZeroDivisionError:
    print("Outer exception: Handled re-raised exception.")


# 9. Best Practices for Exception Handling
# - Be specific about the exception type.
# - Avoid catching generic exceptions unless necessary.
# - Use the `finally` block to clean up resources.
# - Don't suppress exceptions unnecessarily.
# - Raise exceptions with meaningful messages.
# - Avoid using exceptions for flow control.


# 10. Exception Hierarchy in Python
# All exceptions are derived from the `BaseException` class. The common hierarchy is:
# BaseException
# ├── Exception
# │   ├── ArithmeticError
# │   │   ├── ZeroDivisionError
# │   │   ├── OverflowError
# │   └── FileNotFoundError, ValueError, etc.
# └── SystemExit, KeyboardInterrupt, etc.

# Example: Catching base classes
try:
    x = 10 / 0
except ArithmeticError as e:
    print(f"Caught an arithmetic error: {e}")


# 11. Logging Exceptions
# Instead of just printing exceptions, use the `logging` module for better error tracking.

import logging
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"An error occurred: {e}")


# 12. Suppressing Exceptions
# The `contextlib.suppress` context manager can be used to suppress specified exceptions.

from contextlib import suppress

with suppress(ZeroDivisionError):
    result = 10 / 0  # No error will be raised


# 13. Advanced Exception Handling: Exception Chaining
# Python supports exception chaining with `raise from`.

try:
    try:
        num = int("not_a_number")
    except ValueError as e:
        raise RuntimeError("Failed to convert input to an integer.") from e
except RuntimeError as e:
    print(f"Chained exception: {e}")


# 14. Summary of Exception Handling
# - Exception handling ensures program stability by managing errors at runtime.
# - Use `try-except` blocks to catch exceptions.
# - Use `else` for code that runs only when no exception occurs.
# - Use `finally` to execute cleanup code.
# - Raise exceptions intentionally when needed.
# - Define custom exceptions for specific error handling.
# - Use best practices for clear, maintainable code.
