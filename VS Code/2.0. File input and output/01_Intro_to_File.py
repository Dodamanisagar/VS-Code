# 01_Intro_to_File.py

# Introduction to File Input and Output in Python

# Opening a File
# The open() function is used to open a file in Python. It takes two arguments: the file name and the mode.
# Modes:
# 'r' - Read mode (default)
# 'w' - Write mode
# 'a' - Append mode
# 'b' - Binary mode
# 't' - Text mode (default)
# 'x' - Create mode (exclusive creation, fails if file exists)

# Example: Opening a file in read mode
file = open('example.txt', 'r')

# Reading from a File
# The read() method reads the entire content of the file.
content = file.read()
print(content)

# Closing a File
# It is important to close the file after performing operations to free up system resources.
file.close()

# Writing to a File
# The write() method writes a string to the file.
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()

# Appending to a File
# The append mode ('a') allows you to add content to the end of the file without overwriting the existing content.
file = open('example.txt', 'a')
file.write('\nAppended text.')
file.close()

# Reading Line by Line
# The readline() method reads one line at a time.
file = open('example.txt', 'r')
line = file.readline()
while line:
    print(line, end='')
    line = file.readline()
file.close()

# Using 'with' Statement
# The 'with' statement is used for resource management. It ensures that the file is properly closed after its suite finishes.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading Lines into a List
# The readlines() method reads all the lines of a file and returns them as a list.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Binary Mode
# Binary mode is used for non-text files like images or executable files.
with open('example.jpg', 'rb') as file:
    content = file.read()
    # Do something with the binary content

# Example Program: Copying a File
def copy_file(source, destination):
    with open(source, 'rb') as src_file:
        content = src_file.read()
    with open(destination, 'wb') as dest_file:
        dest_file.write(content)

copy_file('example.jpg', 'copy_example.jpg')

# Example Program: Counting Lines, Words, and Characters in a File
def count_file_content(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_lines, num_words, num_chars

lines, words, chars = count_file_content('example.txt')
print(f'Lines: {lines}, Words: {words}, Characters: {chars}')


