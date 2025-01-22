import subprocess
import os

def main():
    # Get the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nChoose a script to run:")
        print("1. Combine Data from a Specified Column")
        print("2. Combine All Worksheets from Workbooks in a Folder")
        print("3. Exit")
        
        choice = input("\nEnter the number of your choice (1, 2, or 3): ").strip()
        
        # Relative paths to the scripts
        script_paths = {
            "1": os.path.join(base_dir, "01_Combine_Columns.py"),
            "2": os.path.join(base_dir, "02_Combine_Worksheets.py"),
        }
        
        if choice == "3":
            print("Exiting the program. Goodbye!")
            break  # Exit the loop
        
        script = script_paths.get(choice)
        if not script:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        # Check if the script exists
        if not os.path.isfile(script):
            print(f"The script '{script}' was not found.")
            continue
        
        try:
            # Execute the chosen script
            print(f"Running script: {script}")
            subprocess.run(["python", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running {os.path.basename(script)}: {e}")
        except FileNotFoundError:
            print(f"The Python executable or script '{os.path.basename(script)}' was not found.")

if __name__ == "__main__":
    main()
