# Abstraction in Python: Concepts, Examples, and Applications

# 1. What is Abstraction?
# Abstraction is the process of hiding implementation details and showing only the essential features of an object.
# It focuses on "what" an object does instead of "how" it does it.
# In Python, abstraction is achieved using abstract classes and abstract methods, provided by the `abc` module.

# Example: Defining Abstract Classes and Methods
from abc import ABC, abstractmethod

# Abstract Base Class (ABC)
class Shape(ABC):  # Inheriting from ABC makes this an abstract class
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation
    
    @abstractmethod
    def perimeter(self):
        pass  # Abstract method with no implementation

# Concrete Class that Implements Abstract Methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Instantiating the Rectangle class
rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())         # Area: 15
print("Perimeter:", rectangle.perimeter())  # Perimeter: 16

# Note: Instantiating an abstract class directly is not allowed and raises a TypeError.


# 2. Why Use Abstraction?
# - To achieve modularity and reduce complexity.
# - To define common behavior in abstract classes and enforce implementation in subclasses.
# - To focus on high-level design without worrying about low-level implementation details.

# Example: Abstract Class Enforcing Method Implementation
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()
print(dog.sound())  # Bark
print(cat.sound())  # Meow


# 3. Key Features of Abstraction in Python
# - Abstract classes cannot be instantiated directly.
# - Abstract classes can have both abstract methods and concrete methods.
# - Subclasses must implement all abstract methods of the parent abstract class.

# Example: Abstract Class with Both Abstract and Concrete Methods
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

    def start_engine(self):  # Concrete method
        print("Starting the engine...")

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

car = Car()
car.start_engine()  # Starting the engine...
print(car.fuel_type())  # Petrol


# 4. Abstract Properties
# Abstract properties can also be defined using the @property decorator along with @abstractmethod.

class Appliance(ABC):
    @property
    @abstractmethod
    def power_consumption(self):
        pass

class WashingMachine(Appliance):
    @property
    def power_consumption(self):
        return "500W"

washing_machine = WashingMachine()
print(washing_machine.power_consumption)  # 500W


# 5. Real-World Example of Abstraction
# Let's consider an abstract class for Payment processing.

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Using the concrete classes
credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
credit_payment.process_payment(100)  # Processing credit card payment of $100
paypal_payment.process_payment(150)  # Processing PayPal payment of $150


# 6. Advantages of Abstraction
# - Promotes code reuse by defining common methods in abstract classes.
# - Ensures consistency by enforcing method implementation in subclasses.
# - Reduces complexity and improves maintainability by focusing on what an object does.

# 7. Disadvantages of Abstraction
# - Increases initial development effort due to the need to define abstract classes and methods.
# - May introduce unnecessary layers if abstraction is overused.

# 8. Difference Between Abstraction and Encapsulation
# - **Abstraction:** Hides implementation details and shows only the essential features.
# - **Encapsulation:** Hides object details through access modifiers (like private or protected variables).

# Example to Illustrate the Difference
class BankAccount(ABC):
    @abstractmethod
    def account_type(self):
        pass

class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"

class Account:
    def __init__(self):
        self.__balance = 1000  # Encapsulation: private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Abstraction
savings = SavingsAccount()
print(savings.account_type())  # Savings Account

# Encapsulation
account = Account()
account.deposit(500)
print(account.get_balance())  # 1500


# 9. Summary of Abstraction in Python
# - Abstraction focuses on exposing only the essential details of a class.
# - It is implemented using abstract classes and methods (from the `abc` module).
# - Abstract classes can contain both abstract and concrete methods.
# - Subclasses must implement all abstract methods of the parent abstract class.
# - Abstract properties can be defined using @property and @abstractmethod.

# 10. Important Points to Remember
# - Abstract classes are defined using the `ABC` class from the `abc` module.
# - The `@abstractmethod` decorator is used to declare methods as abstract.
# - Abstract classes ensure that derived classes implement specific methods.
# - Abstract classes can include concrete methods and properties for shared functionality.

