# pip install pandas openpyxl
# This code will combine data from multiple Excel files in a folder based on specified column names and save the consolidated data to a new Excel file.
import os
import pandas as pd

def combine_excel_data(folder_path, column_names, output_file):
    # List to store DataFrames for efficient concatenation
    data_frames = []

    try:
        # Loop through all files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.xlsx') or file_name.endswith('.xls') or file_name.endswith('.xlsm'):
                file_path = os.path.join(folder_path, file_name)
                
                try:
                    # Load the Excel file
                    excel_file = pd.ExcelFile(file_path)
                    
                    # Loop through each sheet in the workbook
                    for sheet_name in excel_file.sheet_names:
                        try:
                            # Read only the required columns
                            sheet_data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=lambda col: col in column_names)
                            
                            # Append to the list if data is available
                            if not sheet_data.empty:
                                data_frames.append(sheet_data)
                        except Exception as e:
                            print(f"Error processing sheet '{sheet_name}' in file '{file_name}': {e}")
                except Exception as e:
                    print(f"Error processing file '{file_name}': {e}")

        # Concatenate all DataFrames in the list
        if data_frames:
            consolidated_data = pd.concat(data_frames, ignore_index=True)
            
            # Ensure the output file is overridden if it exists
            if os.path.exists(output_file):
                os.remove(output_file)
            
            # Save the consolidated data
            consolidated_data.to_excel(output_file, index=False)
            print(f"Data successfully saved to {output_file}")
        else:
            print("No data matching the specified column names was found.")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: The folder path '{folder_path}' does not exist. {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: Permission denied. {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define parameters
folder_path = r"D:\Data Analyst\6. Python\VS Code\Proj\0. Files to combine"  # Path to folder containing Excel files
column_names = ['age', 'name', 'data']  # Replace with column names to extract
output_file = r"D:\Data Analyst\6. Python\VS Code\Proj\combine.xlsx"  # Output file path

# Run the function
combine_excel_data(folder_path, column_names, output_file)
