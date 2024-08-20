import pandas as pd
import os

# Define the main folder path containing all the year-specific folders
main_folder_path = r'C:\Users\Dell\Desktop\FDS DATA'

# Define the latitude and longitude range
lat_min, lat_max = 8.5, 37.5
lon_min, lon_max = 68.5, 97.5

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

            # Filter the data based on latitude and longitude range
            filtered_data = data[(data['lat'] >= lat_min) & (data['lat'] <= lat_max) &
                                 (data['lon'] >= lon_min) & (data['lon'] <= lon_max)]

            if filtered_data.empty:
                continue  # Skip if no data falls within the specified range

            # Add a 'Year' column based on the folder name (which represents the year)
            filtered_data['Year'] = year_folder

            # Extract the month from the file name (assuming the month is in the file name)
            month = file_name.split('.')[0]  # Adjust this based on your file naming convention
            filtered_data['Month'] = month

            all_data.append(filtered_data)

# Concatenate all data into a single DataFrame
if all_data:
    merged_data = pd.concat(all_data, ignore_index=True)

    # Save the merged DataFrame to a new Excel file
    output_path = r'C:\Users\Dell\Desktop\FDS DATA\filtered_data.xlsx'
    merged_data.to_excel(output_path, index=False)
    print(f"Filtered data successfully merged and saved to {output_path}")
else:
    print("No data to merge.")
