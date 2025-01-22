# Detailed Notes on the `os` Module in Python

"""
The `os` module in Python provides a way of using operating system-dependent functionality like file and directory operations, environment variables, and more. Below is a comprehensive guide with examples.
"""

import os

# ---------------------------------------------------------------
# 1. WORKING WITH FILES AND DIRECTORIES
# ---------------------------------------------------------------

# 1.1 Get Current Working Directory
print("Current Working Directory:", os.getcwd())

# 1.2 Change the Current Working Directory
# Example: Changing to the parent directory
parent_directory = os.path.dirname(os.getcwd())
os.chdir(parent_directory)
print("Changed Working Directory:", os.getcwd())

# 1.3 List Files and Directories
# Example: Listing files in the current directory
print("Files and Directories:", os.listdir())

# 1.4 Create a Directory
# Example: Creating a new directory called 'example_folder'
os.mkdir('example_folder')
print("'example_folder' created.")

# 1.5 Create Nested Directories
# Example: Creating nested directories 'example_folder/nested_folder'
os.makedirs('example_folder/nested_folder', exist_ok=True)
print("'example_folder/nested_folder' created.")

# 1.6 Remove a Directory
# Example: Removing a directory (it must be empty)
os.rmdir('example_folder/nested_folder')
print("'example_folder/nested_folder' removed.")

# 1.7 Remove Nested Directories
# Example: Removing all nested directories
os.removedirs('example_folder')
print("'example_folder' and its nested folders removed.")

# 1.8 Check if a Path Exists
path = 'example_folder'
print("Does path exist?", os.path.exists(path))

# 1.9 Check if a Path is a File or Directory
print("Is it a file?", os.path.isfile(path))
print("Is it a directory?", os.path.isdir(path))

# ---------------------------------------------------------------
# 2. FILE OPERATIONS
# ---------------------------------------------------------------

# 2.1 Rename a File or Directory
# Example: Renaming a file
with open('example_file.txt', 'w') as f:
    f.write('This is a test file.')
os.rename('example_file.txt', 'renamed_file.txt')
print("File renamed to 'renamed_file.txt'.")

# 2.2 Remove a File
os.remove('renamed_file.txt')
print("'renamed_file.txt' removed.")

# ---------------------------------------------------------------
# 3. WORKING WITH ENVIRONMENT VARIABLES
# ---------------------------------------------------------------

# 3.1 Get an Environment Variable
print("PATH environment variable:", os.environ.get('PATH'))

# 3.2 Set an Environment Variable
os.environ['MY_VARIABLE'] = 'Hello, World!'
print("Custom Environment Variable:", os.environ.get('MY_VARIABLE'))

# ---------------------------------------------------------------
# 4. PATH MANIPULATION USING `os.path`
# ---------------------------------------------------------------

# 4.1 Join Paths
# Example: Creating a file path
file_path = os.path.join('example_folder', 'my_file.txt')
print("Joined Path:", file_path)

# 4.2 Get the Directory Name of a Path
print("Directory Name:", os.path.dirname(file_path))

# 4.3 Get the Base Name of a Path
print("Base Name:", os.path.basename(file_path))

# 4.4 Split a Path into Directory and File Name
print("Split Path:", os.path.split(file_path))

# 4.5 Check if a Path is Absolute
print("Is Absolute Path:", os.path.isabs(file_path))

# 4.6 Get the Absolute Path
print("Absolute Path:", os.path.abspath(file_path))

# 4.7 Split File Extension
print("File Extension:", os.path.splitext(file_path))

# ---------------------------------------------------------------
# 5. SYSTEM OPERATIONS
# ---------------------------------------------------------------

# 5.1 Execute a Shell Command
# Example: Listing files using the system shell
os.system('dir' if os.name == 'nt' else 'ls')

# 5.2 Get System-Specific Constants
print("OS Name:", os.name)  # e.g., 'posix' for Linux/Mac, 'nt' for Windows

# ---------------------------------------------------------------
# 6. WALKING THROUGH A DIRECTORY TREE
# ---------------------------------------------------------------

# os.walk() generates the file names in a directory tree, including subdirectories.
for root, dirs, files in os.walk('.'):  # Start from the current directory
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
    print("------------------")

# ---------------------------------------------------------------
# NOTES
# ---------------------------------------------------------------

"""
- The `os` module is cross-platform but some functions behave differently on different operating systems.
- Always handle exceptions (like `FileNotFoundError`, `PermissionError`) when working with files and directories.
- Use `os.path` for safe and consistent path manipulations.
"""
