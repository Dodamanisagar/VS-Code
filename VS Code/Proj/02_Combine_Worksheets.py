import os
import pandas as pd
from openpyxl import Workbook

def combine_excel_sheets(folder_path, output_file):
    """
    Combines all worksheets from all Excel files in the specified folder into one Excel workbook.

    :param folder_path: Path to the folder containing Excel files.
    :param output_file: Full path (including filename) of the output combined workbook.
    """
    try: 
        # Check if folder exists
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Get all Excel files in the folder
        excel_files = [file for file in os.listdir(folder_path) if file.endswith(('.xls', '.xlsx', '.xlsm'))]
        if not excel_files:
            raise FileNotFoundError("No Excel files found in the specified folder.")

        # Create a new workbook for combined data
        combined_workbook = Workbook()
        combined_workbook.remove(combined_workbook.active)  # Remove the default sheet

        for excel_file in excel_files:
            file_path = os.path.join(folder_path, excel_file)
            try:
                # Read all sheets in the workbook
                sheets = pd.read_excel(file_path, sheet_name=None)  # Dictionary with sheet names as keys
                for sheet_name, data in sheets.items():
                    # Add each sheet to the combined workbook
                    sheet_data = combined_workbook.create_sheet(title=f"{os.path.splitext(excel_file)[0]}_{sheet_name[:30]}")
                    for row in data.itertuples(index=False, name=None):
                        sheet_data.append(row)
            except Exception as e:
                print(f"Error reading {excel_file}: {e}")

        # Save the combined workbook
        combined_workbook.save(output_file)
        print(f"Combined workbook saved as '{output_file}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_folder_path = r"D:\Data Analyst\6. Python\VS Code\Proj\0. Files to combine"  # Folder containing input Excel files
output_file_path = r"D:\Data Analyst\6. Python\VS Code\Proj\combined_workbook.xlsx"  # Full path for the output file

combine_excel_sheets(input_folder_path, output_file_path)
