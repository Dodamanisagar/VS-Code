"""
# Recursion in Python

## What is Recursion?
Recursion is a programming concept where a function calls itself in order to solve a problem. It breaks a problem into smaller sub-problems until a base case is reached.

### Key Components of Recursion:
1. **Base Case:** The condition under which the recursion stops. Without a base case, the recursion would continue indefinitely, leading to a stack overflow.
2. **Recursive Case:** The part of the function where it calls itself to solve the smaller version of the problem.

## How Recursion Works
Each recursive call adds a new layer to the call stack. Once the base case is reached, the function returns values, and the call stack starts to unwind.

### Example of Call Stack:
For a recursive function calculating factorial(3):
1. factorial(3)
2. factorial(2)
3. factorial(1) [Base Case]
4. Unwind the stack: factorial(1) -> factorial(2) -> factorial(3)

## Example 1: Factorial Calculation
### Factorial Formula:
Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1

### Recursive Implementation:
"""
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
# Test the function
print(factorial(5))  # Output: 120


## Example 2: Fibonacci Series
### Fibonacci Formula:
# The nth Fibonacci number = (n-1)th Fibonacci + (n-2)th Fibonacci
# Base cases:
# - Fibonacci(0) = 0
# - Fibonacci(1) = 1

### Recursive Implementation:

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
for i in range(10):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34


## Example 3: Sum of a List
### Problem:
# Calculate the sum of all elements in a list recursively.

### Recursive Implementation:
def recursive_sum(numbers):
    # Base case
    if len(numbers) == 0:
        return 0
    # Recursive case
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# Test the function
nums = [1, 2, 3, 4, 5]
print(recursive_sum(nums))  # Output: 15


## Pros and Cons of Recursion
### Pros:
# 1. Simplifies code for problems that are naturally recursive (e.g., tree traversal, factorial).
# 2. Reduces the need for explicit loops.

### Cons:
# 1. Higher memory usage due to the call stack.
# 2. Slower for large inputs (can lead to stack overflow).
# 3. May require optimization (e.g., memoization) for efficiency.


## Summary
# - Recursion is a function calling itself to solve smaller sub-problems.
# - Always include a base case to prevent infinite recursion.
# - Suitable for problems like factorial, Fibonacci, and tree traversal.


