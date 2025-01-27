# Introduction to Functions in Python

# A function is a block of organized, reusable code that is used to perform a single, related action. 
# Functions provide better modularity for your application and a high degree of code reusing.

# Defining a Function
# You can define functions to provide the required functionality. Here are simple rules to define a function in Python:
# 1. Function blocks begin with the keyword `def` followed by the function name and parentheses ( ( ) ).
# 2. Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
# 3. The first statement of a function can be an optional statement - the documentation string of the function or docstring.
# 4. The code block within every function starts with a colon (:) and is indented.
# 5. The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

# Example of a simple function
def greet(name):
    """This function greets the person passed in as a parameter"""
    print(f"Hello, {name}!")

# Calling a function
greet("Alice")

""" 
In Python, methods and functions are similar but have some key differences:

Functions
- Definition: A function is a block of reusable code that performs a specific task. It is defined using the def keyword.
- Usage: Functions can be called independently and are not tied to any object.
- Example:
  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))

Methods
- Definition: A method is a function that is associated with an object. Methods are defined within a class and operate on instances of that class.
- Usage: Methods are called on objects and can access and modify the object's attributes.
- Example:
  class Person:
      def __init__(self, name):
          self.name = name

      def greet(self):
          return f"Hello, {self.name}!"

  person = Person("Alice")
  print(person.greet())

Key Differences
- Association: Functions are standalone, while methods are associated with class instances.
- Calling: Functions are called by their name, whereas methods are called on objects using the dot notation (e.g., object.method()).
- Access: Methods can access and modify the attributes of the object they belong to, while functions cannot.
"""

# Function with return statement
def add(a, b):
    """This function returns the sum of two numbers"""
    return a + b

# Calling the function and printing the result
result = add(5, 3)
print(f"The sum is: {result}")

# Function with default arguments
def greet_with_default(name="Guest"):
    """This function greets the person with a default name if no name is provided"""
    print(f"Hello, {name}!")

# Calling the function without an argument
greet_with_default()

# Calling the function with an argument
greet_with_default("Bob")

# Function with variable-length arguments
def greet_multiple(*names):
    """This function greets multiple people"""
    for name in names:
        print(f"Hello, {name}!")

# Calling the function with multiple arguments
greet_multiple("Alice", "Bob", "Charlie")

# Recursive Function
# A recursive function is a function that calls itself during its execution. This enables the function to repeat itself several times, outputting the result and the end of each iteration.

# Example of a recursive function to calculate factorial
def factorial(n):
    """This function returns the factorial of a given number"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the recursive function
print(f"The factorial of 5 is: {factorial(5)}")

# Lambda Functions
# Lambda functions are small anonymous functions defined using the lambda keyword. They can have any number of arguments but only one expression.

# Example of a lambda function
square = lambda x: x * x

# Calling the lambda function
print(f"The square of 4 is: {square(4)}")

# Higher-order functions
# Functions that take other functions as arguments or return them as results are called higher-order functions.

# Example of a higher-order function
def apply_function(func, value):
    """This function applies a given function to a value"""
    return func(value)

# Using the higher-order function with a lambda function
print(f"The result is: {apply_function(lambda x: x * 2, 5)}")
