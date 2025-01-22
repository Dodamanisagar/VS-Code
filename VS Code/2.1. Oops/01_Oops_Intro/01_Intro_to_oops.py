from abc import ABC, abstractmethod

# 01_Intro_to_oops.py

# Introduction to Object-Oriented Programming (OOP) in Python

# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure the code.
# It allows for better organization, reusability, and abstraction.

# Key Concepts of OOP:
# 1. Class
# 2. Object 
# 3. Inheritance
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction

# The __init__() function:
# The __init__() function, also known as the initializer or constructor, is a special method in Python classes.
# It is automatically called when a new instance of the class is created.
# The purpose of the __init__() function is to initialize the attributes of the class.
# It can take any number of arguments, but the first argument must always be 'self', which refers to the instance being created.

# Example:
# class MyClass:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2

# In this example, when an instance of MyClass is created, the __init__() function initializes the attributes attribute1 and attribute2 with the values passed to it.

# 1. Class:
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):#Dunder method
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# 2. Object:
# An object is an instance of a class. It is created using the class constructor.

# Creating instances of the Dog class
mikey = Dog("Mikey", 6)
lucy = Dog("Lucy", 3)

# Accessing class attributes
print(mikey.species)  # Output: Canis familiaris

# Accessing instance attributes
print(mikey.name)  # Output: Mikey
print(mikey.age)   # Output: 6

# Calling instance methods
print(mikey.description())  # Output: Mikey is 6 years old
print(mikey.speak("Woof Woof"))  # Output: Mikey says Woof Woof

# 3. Inheritance:
# Inheritance allows a class to inherit attributes and methods from another class.

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

# Creating an instance of GoldenRetriever
buddy = GoldenRetriever("Buddy", 9)
print(buddy.description())  # Output: Buddy is 9 years old
print(buddy.speak())  # Output: Buddy says Bark

# 4. Polymorphism:
# Polymorphism allows methods to do different things based on the object it is acting upon.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound="Meow"):
        return f"{self.name} says {sound}"

# Creating instances of Dog and Cat
fido = Dog("Fido", 4)
whiskers = Cat("Whiskers", 2)

# Demonstrating polymorphism
for pet in (fido, whiskers):
    print(pet.speak())

# 5. Encapsulation:
# Encapsulation restricts access to certain attributes and methods to prevent data from being modified directly.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Creating an instance of Person
john = Person("John", 30)
print(john.get_name())  # Output: John
print(john.get_age())   # Output: 30
john.set_age(35)
print(john.get_age())   # Output: 35

# 6. Abstraction:
# Abstraction hides the complex implementation details and shows only the essential features of the object.


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the abstract method
print(dog.make_sound())  # Output: Woof Woof
print(cat.make_sound())  # Output: Meow