# Static Methods in Python: From Basic to Advanced

# 1. Static Method Syntax
# Static methods are defined using the @staticmethod decorator. They don't require self or cls as the first parameter.
class ClassName:
    @staticmethod
    def method_name(parameters):
        # method implementation
        pass


# 2. Basic Concepts of Static Methods:
# Static methods belong to the class rather than an instance of the class.
# They don't require an instance to be called and can be accessed using the class name.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Calling Static Methods
# Static methods can be called using the class name directly
print(Calculator.add(10, 5))          # 15
print(Calculator.subtract(10, 5))     # 5
print(Calculator.multiply(10, 5))     # 50
print(Calculator.divide(10, 5))       # 2.0


# 3. Why Use Static Methods?
# Static methods are useful when:
# - Performing utility functions
# - Grouping related functions in a class
# They don’t require access to instance or class-level attributes.

# Example: Static methods can be used for mathematical or utility functions that don’t rely on instance data.

# 4. Difference Between Instance Methods, Class Methods, and Static Methods

# Instance Method Example:
# Instance methods are bound to an object, and they take `self` as the first parameter, allowing access to instance data.
class MyClass:
    def instance_method(self):
        print(self)

# Class Method Example:
# Class methods are bound to the class, and they take `cls` as the first parameter, allowing access to class-level data.
class MyClassWithClassMethod:
    @classmethod
    def class_method(cls):
        print(cls)

# Static Method Example:
# Static methods are bound to the class, but they don’t take `self` or `cls` as the first parameter.
class MyClassWithStaticMethod:
    @staticmethod
    def static_method():
        print("Static method called!")


# 5. Practical Example of Static Methods
# Static methods can be used to implement utility functions, like checking if a year is a leap year.

class DateUtils:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

print(DateUtils.is_leap_year(2024))  # True
print(DateUtils.is_leap_year(2023))  # False


# 6. Advanced Usage of Static Methods

# Static Methods for Utility Functions
# A static method can be used in a class to group related utility functions that don't rely on the instance or class.
class Vehicle:
    @staticmethod
    def fuel_efficiency(fuel, distance):
        return distance / fuel
    
    @classmethod
    def calculate_efficiency(cls, fuel, distance):
        # This class method calls the static method to calculate fuel efficiency
        print(f"Fuel Efficiency: {cls.fuel_efficiency(fuel, distance)} km/l")

# Calling class method, which uses the static method internally
Vehicle.calculate_efficiency(10, 500)  # Fuel Efficiency: 50.0 km/l


# Static Methods and Inheritance
# Static methods are inherited just like other methods, but they don’t rely on instance data.
class Animal:
    @staticmethod
    def sound():
        return "Some generic animal sound"

class Dog(Animal):
    @staticmethod
    def sound():
        return "Bark"

print(Animal.sound())  # Some generic animal sound
print(Dog.sound())     # Bark


# 7. Advantages of Static Methods:
# - No dependency on class/instance: Static methods can be called without creating an instance.
# - Cleaner code: Helps in organizing related functions inside a class.
# - Improved performance: Static methods are generally faster because they don't need an instance of the class.

# 8. Disadvantages of Static Methods:
# - No access to instance or class state.
# - Less flexible than instance methods in certain situations.


# 9. Static Method vs Class Method vs Instance Method

# Demonstrating the differences between static, class, and instance methods
class Vehicle:
    @staticmethod
    def static_method():
        return "Static method"
    
    @classmethod
    def class_method(cls):
        return "Class method"
    
    def instance_method(self):
        return "Instance method"

# Outputting the differences in methods
vehicle = Vehicle()
print(vehicle.static_method())  # Static method
print(vehicle.class_method())   # Class method
print(vehicle.instance_method())  # Instance method


# 10. Conclusion
# - Static methods are used for functions that don't require access to instance or class state.
# - They are helpful for utility functions and grouping logically related functions.
# - Static methods are efficient but less flexible compared to instance methods.
