# pp install cryptography
from cryptography.fernet import Fernet
import os

# Function to write a new key to 'key.key'
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'key.key'.")

# Function to load the key from 'key.key'
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Check if the key file exists; if not, create it
if not os.path.exists("key.key"):
    write_key()

# Load the key and combine it with the master password
master_pwd = input("Enter master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key[:44])  # Truncate key to 44 bytes (required by Fernet)

# View passwords for a specific site
def view(site_name):
    try:
        with open("password.text", "r") as f:
            found = False
            for line in f.readlines():
                site, pwd = line.strip().split("|")
                if site.strip() == site_name:
                    print(f"Site: {site.strip()}, Password: {fer.decrypt(pwd.encode()).decode()}")
                    found = True
                    break
            if not found:
                print("No password for that site.")
    except FileNotFoundError:
        print("Password file not found. Please add a password first.")
    except Exception as e:
        print("An error occurred while retrieving the password:", e)

# Add a new site and password
def add():
    site = input("Enter site name: ")
    pwd = input("Enter password: ")
    try:
        with open("password.text", "a") as f:
            f.write(site.strip() + " | " + fer.encrypt(pwd.encode()).decode() + "\n")
        print("Password saved successfully.")
    except Exception as e:
        print("An error occurred while saving the password:", e)

# Main program logic
if master_pwd == "1234":
    mode = input("Do you want to store a password or retrieve it? ").lower()
    if mode == "store":
        add()
    elif mode == "retrieve":
        retreive=input("you want to retrieve all passwords or specific ? all / specific : ")
        if retreive=="all":
            view()
        elif retreive=="specific":
            site_name = input("Enter the specific site name: ")
            view(site_name) 
    else:
        print("Invalid mode. Please select 'store' or 'retrieve'.")
else:
    print("Invalid Master Password.")
