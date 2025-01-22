"""
This module demonstrates different types of inheritance in Python with examples.
    Inheritance is a mechanism in object-oriented programming that allows a class to inherit attributes and methods from another class. The class that inherits is called the derived or child class, and the class being inherited from is called the base or parent class.
Types of Inheritance:
1. Single Inheritance:
    Single inheritance allows a derived class to inherit from a single base class.
    
2. Multiple Inheritance:
    (or) Multiple inheritance allows a derived class to inherit from more than one base class.
    
3. Multilevel Inheritance:
    (or) Multilevel inheritance allows a derived class to inherit from another derived class, forming a chain of inheritance.
    
4. Hierarchical Inheritance:
    (or) Hierarchical inheritance allows multiple derived classes to inherit from a single base class.
    
5. Hybrid Inheritance:
    (or) Hybrid inheritance is a combination of two or more types of inheritance.
  
"""

# Inheritance in Python: Concepts and Types

# 1. What is Inheritance?
# Inheritance is a mechanism in object-oriented programming where one class (child) can inherit attributes and methods from another class (parent).
# The class that inherits is called the derived or child class, and the class being inherited from is called the base or parent class.
# It promotes code reuse and hierarchical class relationships.

# Syntax:
# class ParentClass:
#     # Parent class definition
#     pass

# class ChildClass(ParentClass):
#     # Child class definition
#     pass

# Example: Basic Inheritance
class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("The dog barks.")

# Creating objects and demonstrating inheritance
dog = Dog()
dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog


# 2. Types of Inheritance in Python

# 2.1 Single Inheritance
# A child class inherits from one parent class.
# (or)Single inheritance allows a derived class to inherit from a single base class.

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def message(self):
        print("Hello from Child!")

child = Child()
child.greet()   # Inherited from Parent
child.message()  # Defined in Child


# 2.2 Multiple Inheritance
# A child class inherits from more than one parent class.
# (or) Multiple inheritance allows a derived class to inherit from more than one base class.

class Father:
    def wisdom(self):
        print("Father shares wisdom.")

class Mother:
    def kindness(self):
        print("Mother shows kindness.")

class Child(Father, Mother):  # Inherits from both Father and Mother
    def talent(self):
        print("Child shows talent.")

child = Child()
child.wisdom()  # From Father
child.kindness()  # From Mother
child.talent()  # Defined in Child


# 2.3 Multilevel Inheritance
# A child class inherits from a parent class, and a grandchild class inherits from the child class.
# (or) Multilevel inheritance allows a derived class to inherit from another derived class, forming a chain of inheritance.

class Grandparent:
    def legacy(self):
        print("Grandparent leaves a legacy.")

class Parent(Grandparent):
    def guidance(self):
        print("Parent provides guidance.")

class Child(Parent):
    def ambition(self):
        print("Child has ambition.")

child = Child()
child.legacy()  # From Grandparent
child.guidance()  # From Parent
child.ambition()  # Defined in Child


# 2.4 Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.
# (or) Hierarchical inheritance allows multiple derived classes to inherit from a single base class.

class Parent:
    def common_trait(self):
        print("Parent has a common trait.")

class Child1(Parent):
    def unique_trait1(self):
        print("Child1 has a unique trait.")

class Child2(Parent):
    def unique_trait2(self):
        print("Child2 has a unique trait.")

child1 = Child1()
child1.common_trait()  # From Parent
child1.unique_trait1()  # Defined in Child1

child2 = Child2()
child2.common_trait()  # From Parent
child2.unique_trait2()  # Defined in Child2


# 2.5 Hybrid Inheritance
# A combination of multiple types of inheritance. Python uses the Method Resolution Order (MRO) to handle such cases.
# (or) Hybrid inheritance is a combination of two or more types of inheritance.

class Base:
    def base_method(self):
        print("Base class method.")

class A(Base):
    def a_method(self):
        print("Class A method.")

class B(Base):
    def b_method(self):
        print("Class B method.")

class C(A, B):  # Inherits from both A and B, which in turn inherit from Base
    def c_method(self):
        print("Class C method.")

c = C()
c.base_method()  # From Base
c.a_method()  # From A
c.b_method()  # From B
c.c_method()  # Defined in C


# 3. Overriding Methods
# A child class can override methods from the parent class.

class Parent:
    def show_message(self):
        print("Message from Parent.")

class Child(Parent):
    def show_message(self):  # Overriding the parent class method
        print("Message from Child.")

child = Child()
child.show_message()  # Calls the overridden method in Child


# 4. Using the super() Function
# The `super()` function is used to call the parent class method in the child class.

class Parent:
    def show_message(self):
        print("Message from Parent.")

class Child(Parent):
    def show_message(self):
        super().show_message()  # Call the parent class method
        print("Message from Child.")

child = Child()
child.show_message()


# 5. Multiple Inheritance and the Method Resolution Order (MRO)
# Python resolves method calls in the order defined by the MRO, which can be viewed using the `mro()` method or the `__mro__` attribute.

class X:
    def method(self):
        print("Method from X")

class Y(X):
    def method(self):
        print("Method from Y")

class Z(X):
    def method(self):
        print("Method from Z")

class A(Y, Z):  # Inherits from both Y and Z
    pass

a = A()
a.method()  # Method Resolution Order determines which method is called
print(A.mro())  # Prints the MRO for class A


# 6. Summary of Inheritance
# - Inheritance allows code reuse and logical class hierarchies.
# - Types include single, multiple, multilevel, hierarchical, and hybrid inheritance.
# - Child classes can override parent class methods.
# - `super()` enables access to parent class methods.
# - MRO is crucial in handling multiple inheritance scenarios.
