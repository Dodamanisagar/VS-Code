# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division (float)
print("Floor Division:", a // b) # Floor Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation
print("-------------------------------------------------*****-----------------------------------------------")
      
# Comparison Operators
print("Comparison Operators")
print("Equal:", a == b)          # Equal
print("Not Equal:", a != b)      # Not Equal
print("Greater than:", a > b)    # Greater than
print("Less than:", a < b)       # Less than
print("Greater than or equal to:", a >= b) # Greater than or equal to
print("Less than or equal to:", a <= b)    # Less than or equal to
print("-------------------------------------------------*****-----------------------------------------------")

# Logical Operators
x = True
y = False
print("Truth Table for AND")
print("x\ty\tx and y")
print(f"{x}\t{y}\t{x and y}")
print(f"{x}\t{not y}\t{x and (not y)}")
print(f"{not x}\t{y}\t{(not x) and y}")
print(f"{not x}\t{not y}\t{(not x) and (not y)}")
print("------------------------------------")


print("Truth Table for OR")
print("x\ty\tx or y")
print(f"{x}\t{y}\t{x or y}")
print(f"{x}\t{not y}\t{x or (not y)}")
print(f"{not x}\t{y}\t{(not x) or y}")
print(f"{not x}\t{not y}\t{(not x) or (not y)}")
print("------------------------------------")

print("Truth Table for NOT")
print("x\tnot x")
print(f"{x}\t{not x}")
print(f"{not x}\t{not (not x)}")
print("------------------------------------")

print("Logical Operators")
print("Logical AND:", x and y)   # Logical AND
print("Logical OR:", x or y)     # Logical OR
print("Logical NOT:", not x)     # Logical NOT
print("-------------------------------------------------*****-----------------------------------------------")

# Bitwise Operators
print("Bitwise Operators")
print("Bitwise AND:", a & b)     # Bitwise AND
print("Bitwise OR:", a | b)      # Bitwise OR
print("Bitwise XOR:", a ^ b)     # Bitwise XOR
print("Bitwise NOT:", ~a)        # Bitwise NOT
print("Bitwise Left Shift:", a << 1) # Bitwise Left Shift
print("Bitwise Right Shift:", a >> 1) # Bitwise Right Shift
print("-------------------------------------------------*****-----------------------------------------------")

# Assignment Operators
print("Assignment Operators")
c = 5
c += 2  # Equivalent to c = c + 2
print("c after += 2:", c)
c -= 2  # Equivalent to c = c - 2
print("c after -= 2:", c)
c *= 2  # Equivalent to c = c * 2
print("c after *= 2:", c)
c /= 2  # Equivalent to c = c / 2
print("c after /= 2:", c)
c %= 2  # Equivalent to c = c % 2
print("c after %= 2:", c)
c **= 2 # Equivalent to c = c ** 2
print("c after **= 2:", c)
c //= 2 # Equivalent to c = c // 2
print("c after //= 2:", c)
print("-------------------------------------------------*****-----------------------------------------------")

# Identity Operators
print("Identity Operators")
print("Is a identical to b?", a is b)       # Identity
print("Is a not identical to b?", a is not b) # Not Identity
print("-------------------------------------------------*****-----------------------------------------------")

# Membership Operators
print("Membership Operators")
lst = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in lst)            # Membership
print("Is 6 not in list?", 6 not in lst)    # Not Membership
print("-------------------------------------------------*****-----------------------------------------------")