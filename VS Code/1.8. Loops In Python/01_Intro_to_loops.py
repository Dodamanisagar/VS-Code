# 01_Intro_to_loops.py
"""
range() function:
- range(stop): Generates a sequence of numbers from 0 to stop - 1.
- range(start, stop): Generates a sequence of numbers from start to stop - 1.
- range(start, stop, step): Generates a sequence of numbers from start to stop - 1, incrementing by step.
Examples:
1. Iterating over a list using a for loop.
2. Iterating over a string using a for loop.
3. Using the range() function to generate sequences of numbers.
4. Using a while loop to execute a block of code as long as a condition is true.
5. Using break and continue statements to control loop execution.
6. Using nested loops to iterate over multiple sequences.
7. Using pass statement as a placeholder in loops.
8. Advanced loop techniques such as looping through a dictionary, using enumerate(), using zip(), list comprehension, dictionary comprehension, and using else with loops.
"""

# Introduction to Loops in Python

# 1. For Loop
# The for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).


# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: Iterating over a string
for letter in "banana":
    print(letter)

# Example: Using the range() function
for i in range(5):
    print(i)

# Example: Using the range() function with start and end parameters
for i in range(2, 6):
    print(i)

# Example: Using the range() function with start, end, and step parameters
for i in range(2, 10, 2):
    print(i)

    # Example: Using else with for loop
    # The else block will be executed after the for loop completes its iteration, unless the loop is terminated by a break statement.

    for i in range(5):
        print(i)
    else:
        print("Loop completed without break")

    # Example: Using else with for loop and break
    for i in range(5):
        if i == 3:
            break
        print(i)
    else:
        print("Loop completed without break")

# 2. While Loop
# The while loop in Python is used to execute a block of code as long as a condition is true.

# Example: Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Example: Using break statement
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1

# Example: Using continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# 3. Nested Loops
# You can use one or more loops inside another loop.

# Example: Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Example: Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# 4. Loop Control Statements
# break: Terminates the loop statement and transfers execution to the statement immediately following the loop.
# continue: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# pass: Used as a placeholder for future code.

# Example: Using pass statement
for i in range(5):
    if i == 3:
        pass
    print(i)

    # 5. Advanced Loop Techniques

    # Example: Looping through a dictionary
    person = {"name": "John", "age": 30, "city": "New York"}
    for key, value in person.items():
        print(f"{key}: {value}")

    # Example: Looping with enumerate()
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")

    # Example: Looping with zip()
    names = ["John", "Jane", "Doe"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

    # Example: List comprehension with loops
    squares = [x**2 for x in range(10)]
    print(squares)

    # Example: Dictionary comprehension with loops
    squares_dict = {x: x**2 for x in range(10)}
    print(squares_dict)

    # Example: Using else with loops
    for i in range(5):
        print(i)
    else:
        print("Loop completed without break")

    # Example: Using else with loops and break
    for i in range(5):
        if i == 3:
            break
        print(i)
    else:
        print("Loop completed without break")