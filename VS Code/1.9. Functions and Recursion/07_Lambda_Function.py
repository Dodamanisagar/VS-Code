# Lambda Functions in Python: From Basic to Advanced

# 1. Lambda Function Syntax
# Lambda functions are small anonymous functions defined using the 'lambda' keyword.
# Syntax: lambda arguments: expression

# Basic Lambda Function Example
# A simple lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # 8


# 2. What are Lambda Functions?
# Lambda functions are used to create small anonymous functions at runtime.
# They are concise and generally used where a function is needed temporarily.
# Lambda functions can take multiple arguments but only have a single expression.
# They are often used in places like sorting, filtering, and mapping.

# Example: Lambda Function as Argument to Higher-Order Functions

# Using lambda with map to square each number in the list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


# 3. Why Use Lambda Functions?
# Lambda functions are useful when:
# - You need a simple function for a short period.
# - You want to avoid creating a separate function using `def`.
# - You need to pass a function as an argument to other functions.
# - You want to make code more compact and readable for small tasks.

# Example: Using lambda to perform a sorting operation based on the second item of a tuple
tuples = [(1, 2), (3, 1), (5, 0)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # [(5, 0), (3, 1), (1, 2)]


# 4. Lambda Functions vs Regular Functions

# Lambda Function Example
multiply = lambda x, y: x * y

# Regular Function Example using def
def multiply_regular(x, y):
    return x * y

# Both functions do the same thing but in different ways.
print(multiply(5, 3))           # 15
print(multiply_regular(5, 3))   # 15


# 5. Lambda Functions with Multiple Arguments
# Lambda functions can take multiple arguments but can only return one expression.

# Example with multiple arguments
multiply_three = lambda x, y, z: x * y * z
print(multiply_three(2, 3, 4))  # 24


# 6. Lambda Functions with Conditional Expressions
# Lambda functions can contain conditional expressions (ternary operator) for more complex logic.

# Example: Using lambda to check if a number is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Even
print(is_even(7))  # Odd


# 7. Lambda Functions in Functional Programming
# Lambda functions are commonly used in functional programming to perform operations such as:
# - Map: Apply a function to all items in an iterable.
# - Filter: Apply a condition to all items in an iterable.
# - Reduce: Apply a rolling computation to sequential pairs of items in an iterable.

# Example: Using lambda with filter to get only even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]

# Example: Using lambda with reduce to get the product of all numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 720


# 8. Lambda Functions in Sorting and Key Functions
# Lambda functions are often used as the key function in sorting operations.

# Example: Sorting a list of dictionaries by a key value
students = [{'name': 'Alice', 'age': 21}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 22}]
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)
# [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 21}, {'name': 'Charlie', 'age': 22}]


# 9. Advantages of Lambda Functions:
# - Concise syntax: Lambda functions are shorter and more readable.
# - Convenient for simple, one-off functions.
# - Useful when passing functions as arguments to other functions like map(), filter(), and sorted().
# - Don't require a name, making them useful in anonymous function scenarios.

# 10. Disadvantages of Lambda Functions:
# - Limited to a single expression, which can make them harder to read for complex logic.
# - Not ideal for functions that require multiple statements or debugging.

# 11. Lambda Function in List Comprehensions
# Lambda functions can also be used within list comprehensions for transforming data.

# Example: Using lambda in a list comprehension to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [lambda x: x**2 for x in numbers]
print([f(5) for f in squared_numbers])  # [25, 25, 25, 25, 25]


# 12. Lambda Function with Default Arguments
# Lambda functions can also have default values for their arguments, just like regular functions.

# Example: Lambda function with default argument
greet = lambda name="Guest": f"Hello, {name}!"
print(greet())          # Hello, Guest!
print(greet("Alice"))   # Hello, Alice!


# 13. Conclusion
# - Lambda functions are useful for quick, simple operations and are often used in higher-order functions like map(), filter(), and reduce().
# - While lambda functions can help make your code concise, avoid using them for complex logic that is better suited to a regular function.
