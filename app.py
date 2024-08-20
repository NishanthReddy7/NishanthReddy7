import yfinance as yf
import pandas as pd
import os

# Download stock data
df = yf.download('BTC', start='2022-01-01', end='2024-01-01')

# Check if data was successfully downloaded
if df.empty:
    print("Data download failed or no data for the specified period.")
else:
    print("Data downloaded successfully:")
    print(df)

    # Save the data to an Excel file
    excel_file = 'Bitcoin_yfinance_data.xlsx'
    df.to_excel(excel_file)

    # Automatically open the Excel file
    os.startfile(excel_file)
