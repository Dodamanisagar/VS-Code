# 3. Type Hinting Enhancements (Python 3.10 & 3.11)
# `|` operator for Union types (Python 3.10)


def divide(x:int|float,
           y:int|float)->int|float:
    if y==0:
        return "Division by zero is not allowed"
    else:
        return x/y

print(divide(10,0))
