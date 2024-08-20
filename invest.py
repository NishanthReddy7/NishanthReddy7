import investpy
"""
# Define the stock ticker, country, and date range
ticker = 'AAPL'  # Example: Apple Inc.
country = 'United States'
start_date = '01/01/2020'
end_date = '01/01/2021'

# Fetch historical data
df = investpy.get_stock_historical_data(stock=ticker, country=country,
                                        from_date=start_date, to_date=end_date)

# Display the data
print(df)

# Optionally, save to CSV
df.to_csv(f'{ticker}_historical_data.csv')
"""
import yfinance as yf

# Download stock data
df = yf.download('AAPL', start='2020-01-01', end='2021-01-01')

# Display the data
print(df)

# Save to CSV
df.to_csv('apple_yfinance_data.csv')
