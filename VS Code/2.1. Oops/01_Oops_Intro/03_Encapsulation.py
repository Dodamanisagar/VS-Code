# Encapsulation in Python: Concepts and Examples

# 1. What is Encapsulation?
# Encapsulation is a fundamental principle of object-oriented programming (OOP) that involves:
# - Bundling data (attributes) and methods (functions) into a single unit, i.e., a class.
# - Controlling access to the internal state of an object to ensure data integrity and security.
# - Hiding implementation details using access specifiers.

# Python supports encapsulation through public, protected, and private attributes.

# Example: Basic Encapsulation
class Example:
    def __init__(self, data):
        self.data = data  # Public attribute

    def display(self):
        print(f"Data: {self.data}")

# Creating an object and accessing attributes/methods
obj = Example("Hello, World!")
obj.display()   # Accessing the method
print(obj.data)  # Directly accessing the public attribute


# 2. Access Modifiers in Encapsulation
# Python provides three levels of access modifiers for encapsulation:
# - Public: Accessible from anywhere (default in Python).
# - Protected: Accessible within the class and subclasses (denoted with a single underscore `_`).
# - Private: Accessible only within the class (denoted with double underscores `__`).

# 2.1 Public Access Modifier
# Public attributes and methods can be accessed from outside the class.

class PublicExample:
    def __init__(self):
        self.public_attribute = "I am public!"

    def public_method(self):
        print("This is a public method.")

obj = PublicExample()
print(obj.public_attribute)  # Accessible
obj.public_method()           # Accessible


# 2.2 Protected Access Modifier
# Protected attributes and methods are indicated with a single underscore `_`.
# They are accessible within the class and its subclasses but should be treated as non-public.

class ProtectedExample:
    def __init__(self):
        self._protected_attribute = "I am protected!"

    def _protected_method(self):
        print("This is a protected method.")

class SubClass(ProtectedExample):
    def access_protected(self):
        print(self._protected_attribute)  # Accessible in subclass
        self._protected_method()          # Accessible in subclass

obj = SubClass()
obj.access_protected()
# Protected attributes/methods can still be accessed directly but are intended for internal use.
print(obj._protected_attribute)  # Not recommended


# 2.3 Private Access Modifier
# Private attributes and methods are indicated with double underscores `__`.
# They are accessible only within the class where they are defined.

class PrivateExample:
    def __init__(self):
        self.__private_attribute = "I am private!"

    def __private_method(self):
        print("This is a private method.")

    def access_private(self):
        # Accessing private attributes/methods within the class
        print(self.__private_attribute)
        self.__private_method()

obj = PrivateExample()
obj.access_private()

# Attempting to access private attributes/methods from outside will result in an AttributeError
# print(obj.__private_attribute)  # Uncomment to see the error


# 3. Name Mangling
# Python uses name mangling to make private attributes accessible in special cases.
# Private attributes/methods are renamed internally as `_ClassName__attributeName`.

class NameMangleExample:
    def __init__(self):
        self.__hidden = "Hidden Value"

obj = NameMangleExample()
# Accessing private attributes using name mangling (not recommended)
print(obj._NameMangleExample__hidden)


# 4. Getter and Setter Methods
# Encapsulation often uses getter and setter methods to control access to private attributes.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance                # Private attribute

    # Getter method for account_holder
    def get_account_holder(self):
        return self.__account_holder

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

    # Getter method for balance
    def get_balance(self):
        return self.__balance

# Using the BankAccount class
account = BankAccount("Alice", 1000)
print(account.get_account_holder())  # Accessing private attribute via getter
print(account.get_balance())         # Accessing balance via getter

account.set_balance(1500)            # Updating balance via setter
print(account.get_balance())


# 5. Benefits of Encapsulation
# - Data Protection: Prevents accidental or unauthorized access to sensitive data.
# - Improved Code Maintainability: Changes to implementation details can be made without affecting external code.
# - Controlled Access: Provides a controlled way to access and modify data using getters and setters.
# - Abstraction: Hides implementation details and exposes only relevant functionality.

# 6. Example: Real-World Application of Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def get_details(self):
        return f"Name: {self.__name}, Salary: ${self.__salary}"

    def update_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary!")

# Creating an employee object
employee = Employee("John", 5000)
print(employee.get_details())  # Accessing private attributes via method

employee.update_salary(6000)  # Updating private attribute via method
print(employee.get_details())

# Attempting to directly access private attributes will fail
# print(employee.__name)  # Uncomment to see the error


# 7. Summary
# - Encapsulation bundles data and methods into a class and restricts direct access to sensitive data.
# - Public, protected, and private access modifiers define the scope of accessibility.
# - Use getter and setter methods for controlled access and modification of private attributes.
# - Encapsulation ensures data security, abstraction, and better code maintainability.
