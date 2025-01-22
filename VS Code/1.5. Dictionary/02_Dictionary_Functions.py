# Dictionary Functions in Python

# 1. len() - Returns the number of items in the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3

# 2. keys() - Returns a view object that displays a list of all the keys in the dictionary
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# 3. values() - Returns a view object that displays a list of all the values in the dictionary
print(my_dict.values())  # Output: dict_values([1, 2, 3])

# 4. items() - Returns a view object that displays a list of dictionary's key-value tuple pairs
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. get() - Returns the value of the specified key. If the key does not exist, returns None (or a specified default value)
print(my_dict.get('b'))  # Output: 2
print(my_dict.get('d', 'Not Found'))  # Output: Not Found

# 6. update() - Updates the dictionary with the specified key-value pairs
my_dict.update({'d': 4, 'e': 5})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 7. pop() - Removes the element with the specified key and returns its value
print(my_dict.pop('a'))  # Output: 1
print(my_dict)  # Output: {'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 8. popitem() - Removes and returns the last inserted key-value pair as a tuple
print(my_dict.popitem())  # Output: ('e', 5)
print(my_dict)  # Output: {'b': 2, 'c': 3, 'd': 4}

# 9. clear() - Removes all items from the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Practice Programs

# Program 1: Count the frequency of each character in a string
def char_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

print(char_frequency("hello world"))

# Program 2: Merge two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}

# Program 3: Create a dictionary from two lists
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
print(lists_to_dict(keys, values))  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}