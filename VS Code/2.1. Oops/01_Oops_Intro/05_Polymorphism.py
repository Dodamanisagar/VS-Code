# Polymorphism in Python: Concepts, Types, and Examples

# 1. What is Polymorphism?
# Polymorphism is a concept in object-oriented programming where the same function or method name can behave differently based on the object or context it is called on.
# The term "Polymorphism" means "many forms."

# Example: A single operation behaves differently on different types of objects
print(len("Python"))  # Output: 6 (String length)
print(len([1, 2, 3, 4]))  # Output: 4 (List length)


# 2. Types of Polymorphism in Python

# 2.1 Duck Typing
# "If it walks like a duck and quacks like a duck, it is a duck."
# Python supports dynamic typing, so objects are determined by their behavior rather than their class.

# Example: Duck Typing
class Bird:
    def sound(self):
        print("Chirp chirp!")

class Dog:
    def sound(self):
        print("Woof woof!")

def make_sound(animal):
    animal.sound()

# Objects with the same method name can be used interchangeably
bird = Bird()
dog = Dog()
make_sound(bird)  # Chirp chirp!
make_sound(dog)   # Woof woof!


# 2.2 Method Overriding
# A subclass provides a specific implementation for a method already defined in its parent class.

# Example: Method Overriding
class Shape:
    def area(self):
        print("Calculating area for a general shape.")

class Circle(Shape):
    def area(self):
        print("Calculating area for a circle.")

shape = Shape()
circle = Circle()
shape.area()   # General implementation
circle.area()  # Specific implementation (Overridden method)


# 2.3 Method Overloading (Achieved using Default Arguments)
# Python does not support method overloading directly, but it can be simulated using default arguments.

# Example: Method Overloading with Default Arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5 (Two arguments)
print(calc.add(2, 3, 4))    # 9 (Three arguments)


# 2.4 Operator Overloading
# Python allows operators to be overloaded to perform different tasks based on the operands.

# Example: Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2  # Using overloaded '+' operator
print(result)  # Output: (6, 8)


# 3. Polymorphism with Inheritance
# Child classes inherit methods from the parent class but can also override them to provide specific behavior.

# Example: Polymorphism with Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

animals = [Animal(), Cat(), Dog()]
for animal in animals:
    animal.speak()  # Each object calls its own version of the method


# 4. Polymorphism with Functions and Objects
# Functions in Python can take objects of different types and execute their behavior.

# Example: Polymorphism with Functions
class Laptop:
    def type(self):
        print("Laptop is for coding.")

class Mobile:
    def type(self):
        print("Mobile is for calling.")

def device_usage(device):
    device.type()

laptop = Laptop()
mobile = Mobile()
device_usage(laptop)  # Laptop is for coding.
device_usage(mobile)  # Mobile is for calling.


# 5. Polymorphism with Abstract Base Classes (ABCs)
# Abstract Base Classes enforce a structure in subclasses, ensuring certain methods are implemented.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Enforces structure and behavior consistency


# 6. Advantages of Polymorphism:
# - Code Reusability: Write generalized code for multiple types of objects.
# - Flexibility: Allows a single interface for interacting with different types of objects.
# - Extensibility: Easy to add new functionality without modifying existing code.

# 7. Summary:
# Polymorphism in Python enables a single function, method, or operator to have multiple forms, making the code versatile and reusable.
# Types of Polymorphism include:
# - Duck Typing
# - Method Overriding
# - Method Overloading (simulated)
# - Operator Overloading
# Polymorphism is a core concept in object-oriented programming, enhancing flexibility and code quality.

