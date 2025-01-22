# The input() function in Python is used to take input from the user.
# It reads a line from input, converts it into a string, and returns it.

# Basic usage:
user_input = input("Enter something: ")
print("You entered:", user_input)

# The input() function can also be used to take numerical input.
# However, the input is always returned as a string, so you need to convert it to the desired type.
age = int(input("Enter your age: "))
print("Your age is:", age)

# Example with float:
height = float(input("Enter your height in meters: "))
print("Your height is:", height)

# Example with multiple inputs:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}. You are {age} years old.") #Formatted String Literals (f-strings) are a way to embed expressions inside string literals, using curly braces {}.

# Note: If the user enters a value that cannot be converted to the specified type (e.g., entering a non-numeric value when an integer is expected), a ValueError will be raised.

# Handling ValueError exception when converting input to a specific type:
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Invalid input! Please enter a numeric value for age.")

# Using input() with a default value (requires additional logic):
default_name = "John Doe"
name = input(f"Enter your name (default is {default_name}): ") or default_name
print(f"Hello, {name}.")

# Using input() with a prompt and stripping whitespace:
user_input = input("Enter something: ").strip() 
print("You entered:", user_input)

# Practice Program 1: Taking multiple inputs and performing arithmetic operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {prod_result}, Quotient: {quot_result}")

# Practice Program 2: Taking a list of numbers as input and finding the average
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
average = sum(numbers) / len(numbers) if numbers else 0
print(f"The average of the entered numbers is: {average}")

# Practice Program 3: Taking a sentence as input and counting the number of words
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"The number of words in the sentence is: {word_count}")

# Practice Program 4: Taking a date as input and printing it in a different format
date_input = input("Enter a date (dd/mm/yyyy): ")
day, month, year = date_input.split('/')
print(f"You entered the date: {year}-{month}-{day}")

# Practice Program 5: Taking a string input and reversing it
string_input = input("Enter a string: ")
reversed_string = string_input[::-1]
print(f"The reversed string is: {reversed_string}")

# Additional Example: Validating input as a specific type
def get_validated_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

valid_number = get_validated_integer("Enter a valid integer: ")
print(f"You entered the valid integer: {valid_number}")

# Additional Example: Password input with hidden characters
import getpass
password = getpass.getpass("Enter your password (hidden): ")
print("Password entered successfully.")
