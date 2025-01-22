"""
# Comprehensive Notes on Python Functions

## What is a Function?
A function is a reusable block of code that performs a specific task. Functions help organize code, make it modular, and reduce redundancy.



## Types of Functions in Python:
1. **Built-in Functions**: Predefined functions like `print()`, `len()`, `max()`, etc.
2. **User-defined Functions**: Custom functions created by users.


## Syntax of a Function:

def function_name(parameters):
    # Docstring (Optional): A brief description of what the function does.
    # Function body
    return result (Optional)


## Example 1: A Simple Function
"""
def greet():
    """This function prints a greeting message."""
    print("Hello, welcome to Python functions!")

greet()

"""



## Parameters and Arguments
**Parameter**: A variable listed inside parentheses in the function definition.
**Argument**: A value passed to the function when it is called.



## Example 2: Function with Parameters and Arguments
"""
def add_numbers(a, b):
    """This function adds two numbers."""
    return a + b

result = add_numbers(5, 3)
print(f"Addition Result: {result}")

"""

---

## Default Parameters
If no argument is provided, default parameters take their specified value.

---

## Example 3: Function with Default Parameters
"""
def greet_person(name="Guest"):
    """This function greets a person with a default name."""
    print(f"Hello, {name}!")

greet_person()  # Uses default value
greet_person("Sagar")  # Overrides default value

"""

---

## Variable-length Arguments
Allows a function to accept any number of arguments:
1. `*args`: Non-keyworded arguments (tuple).
2. `**kwargs`: Keyworded arguments (dictionary).

---

## Example 4: Function with *args
"""
def print_numbers(*args):
    """This function prints all the numbers passed as arguments."""
    for number in args:
        print(number, end=" ")

print_numbers(1, 2, 3, 4)

"""

---

## Example 5: Function with **kwargs
"""
def print_details(**kwargs):
    """This function prints key-value pairs of details."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Sagar", role="Fresher", language="Python")

"""

---

## Returning Multiple Values
A function can return multiple values using tuples.

---

## Example 6: Returning Multiple Values
"""
def calculate(a, b):
    """This function returns the sum, difference, and product of two numbers."""
    return a + b, a - b, a * b

sum_result, diff_result, prod_result = calculate(7, 3)
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {prod_result}")

"""

---

## Lambda Functions
- Anonymous (unnamed) functions created using the `lambda` keyword.
- Syntax: `lambda arguments: expression`

---

## Example 7: Lambda Function
"""
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"Sum of 3 and 7: {add(3, 7)}")

"""

---

## Scope of Variables
1. **Local Scope**: Variables defined inside a function.
2. **Global Scope**: Variables defined outside any function.
3. Use `global` keyword to modify global variables inside a function.

---

## Example 8: Scope of Variables
"""
x = 10  # Global variable

def modify_variable():
    global x
    x += 5  # Modifying global variable
    print(f"Inside function, x: {x}")

modify_variable()
print(f"Outside function, x: {x}")

"""

---

## Nested Functions
Functions defined inside other functions.

---

## Example 9: Nested Functions
"""
def outer_function():
    """This is the outer function."""
    def inner_function():
        """This is the inner function."""
        print("Hello from the inner function!")
    inner_function()

outer_function()

"""

---

## Recursion
A function calling itself to solve smaller instances of the same problem.

---

## Example 10: Recursive Function
"""
def factorial(n):
    """This function calculates the factorial of a number using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

"""

---

## Decorators
Special functions that modify the behavior of another function.

---

## Example 11: Using a Decorator
"""
def decorator_function(original_function):
    """A simple decorator."""
    def wrapper_function():
        print("Wrapper executed before the original function.")
        original_function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

"""

---

## Static Methods
A method that belongs to a class but does not operate on an instance of the class or the class itself. Defined using the `@staticmethod` decorator.

---

## Example 12: Static Method
"""
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        """This method adds two numbers."""
        return a + b

result = MathUtils.add_numbers(5, 7)
print(f"Addition Result: {result}")  # Output: 12

"""
## Summary
1. Functions are essential for code reusability and readability.
2. They can have parameters, default values, and return values.
3. Advanced concepts include recursion, decorators, static methods, and lambda functions.

"""
