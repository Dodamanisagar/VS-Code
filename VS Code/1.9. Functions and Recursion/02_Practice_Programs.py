# 1. Function to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the factorial function
print(factorial(5))  # Output: 120

# 2. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
# Test the is_prime function
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False

# 3. Function to find the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the fibonacci function
print(fibonacci(6))  # Output: 8

# 4. Function to reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Test the reverse_string function
print(reverse_string("hello"))  # Output: "olleh"

# 5. Function to find the greatest common divisor (GCD) of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test the gcd function
print(gcd(48, 18))  # Output: 6