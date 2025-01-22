
# Decorators in Python

# A decorator is a function that allows you to modify the behavior of another function or method.
# It is a higher-order function, meaning it takes a function as an argument and returns a new function.

# Syntax of a decorator:
# The general syntax for a decorator is as follows:

# def decorator_function(original_function):
#     def wrapper_function():
#         # Modify behavior or add functionality
#         return original_function()
#     return wrapper_function

# Example of a decorator:

def decorator_function(original_function):
    def wrapper_function():
        print("Function is about to run...")
        return original_function()
    return wrapper_function

def display():
    print("Display function is running!")

# Applying the decorator to the display function
decorated_display = decorator_function(display)
decorated_display()

# A shorthand syntax to apply decorators using the "@" symbol is:

@decorator_function
def show():
    print("Show function is running!")

show()

# Output:
# Function is about to run...
# Display function is running!
# Function is about to run...
# Show function is running!
