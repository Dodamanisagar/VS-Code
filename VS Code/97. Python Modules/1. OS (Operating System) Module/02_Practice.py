import os
parent_directory = os.path.dirname(os.getcwd())
os.chdir(parent_directory)
print("Changed Working Directory:", os.getcwd())