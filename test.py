import os
import pandas as pd

# Define the directory where your folders are located
base_dir = r'C:\Users\Dell\Desktop\FDS DATA'  # Update this to your actual path

# Latitude and Longitude filters
lat_min, lat_max = 8.5, 37.5
lon_min, lon_max = 68.5, 97.5

# Prepare an empty dictionary to store data by month
data_by_month = {i: [] for i in range(1, 13)}

# Loop through each year's folder
for year in range(2005, 2006):
    year_folder = os.path.join(base_dir, str(year))

    if not os.path.exists(year_folder):
        continue

    # Loop through each month's file in the year folder
    for month in range(1, 13):
        file_path = os.path.join(year_folder, f'{month:02}.CSV')  # Assuming files are named as '01.CSV', '02.CSV', etc.

        if os.path.exists(file_path):
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Filter based on Latitude and Longitude
            filtered_df = df[
                (df['Latitude'] >= lat_min) & (df['Latitude'] <= lat_max) &
                (df['Longitude'] >= lon_min) & (df['Longitude'] <= lon_max)
                ]

            # Append the filtered data to the respective month
            data_by_month[month].append(filtered_df)

# After collecting all the data, merge each month's data and save to a new Excel file
with pd.ExcelWriter('merged_filtered_data.xlsx') as writer:
    for month in range(1, 13):
        if data_by_month[month]:  # Check if there's any data for this month
            # Concatenate all dataframes for this month
            month_df = pd.concat(data_by_month[month])
            # Write to Excel, with each month in a separate sheet
            month_df.to_excel(writer, sheet_name=f'Month_{month:02}', index=False)
