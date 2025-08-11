import sys
import time
import yfinance as yf

# Note: Used yfinance due to persistent 404 errors and bot detection when scraping Yahoo Finance with requests/BeautifulSoup.

# Check argument count
if len(sys.argv) != 3:
    raise Exception("Usage: python3 financial.py TICKER 'Field Name'")

ticker = sys.argv[1]
field_name = sys.argv[2]

# Sleep for 5 seconds as required
time.sleep(5)

# Fetch financial data
try:
    stock = yf.Ticker(ticker)
    financials = stock.financials
except Exception as e:
    raise Exception(f"Failed to fetch financial data for ticker {ticker}: {str(e)}")

# Check if financials data is available
if financials.empty:
    raise Exception(f"No financial data found for ticker {ticker}")

# Check if the field exists
if field_name not in financials.index:
    raise Exception(f"Field '{field_name}' not found for {ticker}. Valid fields include: {', '.join(financials.index)}")

# Extract values
values = [field_name]  # Start with the user-provided field name
row = financials.loc[field_name]

# Convert values to strings, remove NaN, and format as integers
for value in row:
    if not isinstance(value, float) or not value != value:  # Check for non-NaN values
        values.append(str(int(value)))

# Ensure at least one value exists
if len(values) == 1:
    raise Exception(f"No valid data found for field '{field_name}' for {ticker}")

# Output the tuple
print(tuple(values))





