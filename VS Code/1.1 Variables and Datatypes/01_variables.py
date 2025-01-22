### Rules for Defining Variables in Python
# Variables in Python are used to store data values.
# Follow these rules and guidelines to define variables correctly.

# ---

#### Rules:
# 1. Start with a Letter or Underscore
#    - A variable name must begin with a letter (a-z, A-Z) or an underscore (_).
#      Examples: my_var, _myVar

# 2. Use Letters, Numbers, and Underscores
#    - After the first character, variable names can include letters, numbers, and underscores.
#      Examples: var1, my_var_2, _temp3

# 3. Case Sensitivity
#    - Variable names are case-sensitive, meaning myVar, MyVar, and myvar are different variables.
#      Examples: count, Count, COUNT

# 4. Avoid Reserved Words
#    - You cannot use Python keywords (reserved words) as variable names.
#      Example: for = 5 (invalid, because "for" is a keyword)

# ---

#### Guidelines (Best Practices):
# 1. Use Descriptive Names
#    - Choose variable names that describe the purpose of the variable.
#      Examples: student_name, total_marks

# 2. Use Snake Case for Multi-word Names
#    - Use underscores to separate words in variable names.
#      Example: total_sales, is_valid_user

# 3. Avoid Single-letter Names (except for temporary variables)
#    - Use single-letter names like i, j, k for loop counters or temporary variables only.
#      Example: for i in range(5)
#      Avoid: a = 100 (use age = 100 instead)

# 4. Do Not Start with Numbers or Special Characters
#    - Variable names cannot start with numbers or symbols like @, $, %.
#      Examples: 1var (invalid), my-var (invalid), @temp (invalid)

# 5. Follow Consistent Naming Conventions
#    - Be consistent in how you name variables throughout your code.

# ---

#### Examples of Valid and Invalid Variable Names
# | Valid Names           | Invalid Names         |
# |-----------------------|-----------------------|
# | my_var               | 2myVar               |
# | _temp_var            | my-var               |
# | total_sales          | my var               |
# | var123               | class (keyword)      |

# ---

#### Example Code

# Valid variable names
student_name = "Alice"
age = 25
_total_sales = 1500.75
is_valid = True
marks_obtained_2024 = 95

# Invalid variable names (uncomment to see errors)
# 2student = "Bob"   # Starts with a number
# my-var = 100       # Contains a hyphen
# class = "Python"   # Uses a reserved keyword

# Case-sensitive examples
student = "John"
Student = "Doe"
print(student)   # Output: John
print(Student)   # Output: Doe

# Example: Basic usage
a = 5
b = 10
result = a + b
print("The sum is:", result)  # Output: The sum is: 15

# ---

#### Keywords in Python
# Reserved words that cannot be used as variable names include:
# False, None, True, and, as, assert, break, class, continue, def, del,
# elif, else, except, finally, for, from, global, if, import, in, is,
# lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# Use the keyword module to see all keywords
import keyword
print(keyword.kwlist)
