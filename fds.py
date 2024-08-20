import pandas as pd
import os

# Define the main folder path containing all the year-specific folders
main_folder_path = r'C:\Users\Dell\Desktop\FDS DATA'

all_data = []

# Loop through each year folder
for year_folder in os.listdir(main_folder_path):
    year_folder_path = os.path.join(main_folder_path, year_folder)

    # Check if the item is a directory (folder)
    if os.path.isdir(year_folder_path):
        print(f"Processing year: {year_folder}")  # Print the current year being processed

        # Loop through all files in the year folder
        for file_name in os.listdir(year_folder_path):
            file_path = os.path.join(year_folder_path, file_name)

            # Read the Excel or CSV file
            if file_name.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            elif file_name.endswith('.csv'):
                data = pd.read_csv(file_path)
            else:
                continue  # Skip files that are not .xlsx or .csv

            print(f"Processing file: {file_name}")  # Check which file is being processed
            print(data.head())  # Preview the first few rows of the data

            # Add a 'Year' column based on the folder name (which represents the year)
            data['Year'] = year_folder

            # Add the month from the file name (assuming the month is in the file name)
            month = file_name.split('.')[0]  # Adjust this based on your file naming convention
            data['Month'] = month

            all_data.append(data)

# Concatenate all data into a single DataFrame
if all_data:
    merged_data = pd.concat(all_data, ignore_index=True)

    # Save the merged DataFrame to a new Excel file
    output_path = r'C:\Users\Dell\Desktop\FDS DATA\merged_data.xlsx'
    merged_data.to_excel(output_path, index=False)
    print(f"Data successfully merged and saved to {output_path}")
else:
    print("No data to merge.")
