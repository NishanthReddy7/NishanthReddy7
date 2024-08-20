import ccxt
import pandas as pd
import os
from datetime import datetime

# Initialize the exchange
exchange = ccxt.binance()  # You can use other exchanges like 'kraken', 'coinbase', etc.

# Define parameters
symbol = 'BTC/USDT'
timeframe = '1d'  # Daily data
since = exchange.parse8601('2021-01-01T00:00:00Z')  # Start date
now = exchange.milliseconds()  # End date (current time)

# Fetch historical data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit=1000)  # You can adjust limit as needed

# Convert to DataFrame
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Display the data
print(df)

# Save the data to an Excel file
excel_file = 'bitcoin_data1.xlsx'
df.to_excel(excel_file)

# Automatically open the Excel file
os.startfile(excel_file)
