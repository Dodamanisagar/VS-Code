# Introduction to Conditional Statements in Python

# Conditional statements are used to perform different actions based on different conditions.
# The most common conditional statements in Python are `if`, `elif`, and `else`.

# 1. if Statement
# The `if` statement is used to test a specific condition. If the condition is true, the block of code inside the `if` statement is executed.

# Syntax:
# if condition:
#     # code to execute if condition is true

# Example:
x = 10
if x > 5:
    print("x is greater than 5")

# 2. elif Statement
# The `elif` statement is short for "else if". It allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions is true.

# Syntax:
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true

# Example:
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")

# 3. else Statement
# The `else` statement is an optional statement and the last statement in the conditional block. It is executed if none of the previous conditions are true.

# Syntax:
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if none of the conditions are true

# Example:
x = 3
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")

# 4. Nested if Statements
# You can use one `if` or `elif` statement inside another `if` or `elif` statement(s).

# Example:
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")

# 5. Conditional Expressions (Ternary Operator)
# Conditional expressions provide a way to write simple `if-else` statements in a single line.

# Syntax:
# value_if_true if condition else value_if_false

# Example:
x = 10
result = "x is greater than 5" if x > 5 else "x is 5 or less"
print(result)

# Summary:
# - Use `if` to specify a block of code to be executed if a condition is true.
# - Use `elif` to specify a new condition to test if the first condition is false.
# - Use `else` to specify a block of code to be executed if all previous conditions are false.
# - Use nested `if` statements to check multiple conditions.
# - Use conditional expressions for simple `if-else` statements in a single line.