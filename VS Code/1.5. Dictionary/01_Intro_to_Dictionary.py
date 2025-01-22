# 01_Intro_to_Dictionary.py

# Introduction to Dictionary in Python
# A dictionary is a collection which is unordered, changeable, and indexed. 
# In Python, dictionaries are written with curly brackets, and they have keys and values.

# Example of a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets.
print(my_dict["name"])  # Output: John

# Change Values
# You can change the value of a specific item by referring to its key name.
my_dict["age"] = 31
print(my_dict["age"])  # Output: 31

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
for key in my_dict:
    print(key, my_dict[key])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the 'in' keyword.
if "name" in my_dict:
    print("Yes, 'name' is one of the keys in the my_dict dictionary")

# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() function.
print(len(my_dict))  # Output: 3

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
my_dict["email"] = "john@example.com"
print(my_dict)

# Removing Items
# There are several methods to remove items from a dictionary:
my_dict.pop("age")  # Removes the item with the specified key name
print(my_dict)

my_dict.popitem()  # Removes the last inserted item
print(my_dict)

del my_dict["city"]  # Removes the item with the specified key name
print(my_dict)

my_dict.clear()  # Empties the dictionary
print(my_dict)  # Output: {}

# Practice Programs

# 1. Create a dictionary with five key-value pairs and print it.
practice_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red",
    "price": 30000
}
print(practice_dict)

# 2. Write a program to update the value of a key in a dictionary.
practice_dict["year"] = 2020
print(practice_dict)

# 3. Write a program to remove a key from a dictionary.
practice_dict.pop("price")
print(practice_dict)

# 4. Write a program to check if a key exists in a dictionary.
if "model" in practice_dict:
    print("Model key exists in the dictionary")

# 5. Write a program to loop through a dictionary and print all key-value pairs.
for key, value in practice_dict.items():
    print(key, value)