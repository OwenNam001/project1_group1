# Common Module for Interest Rate data retrieval

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import fred_api_key
from fredapi import Fred


# Initialize the FRED API key
fred = Fred(api_key=fred_api_key)
# data = fred.search('interest rate')

# Fetch data for the Federal Funds Effective Rate
series_id = 'FEDFUNDS'  # Series ID for the Federal Funds Rate
InterestRate_Data = fred.get_series(series_id, observation_start='2010-01-01', observation_end='2019-12-31')

# Convert the series data into a DataFrame
InterestRate_Data_df = pd.DataFrame(InterestRate_Data, columns=['Rate'])
InterestRate_Data_df.reset_index(inplace=True)
InterestRate_Data_df.columns = ['Date', 'Rate']

# Extract 'Year' and 'Month' from 'Date'
InterestRate_Data_df['Year'] = InterestRate_Data_df['Date'].dt.year
InterestRate_Data_df['Month'] = InterestRate_Data_df['Date'].dt.strftime('%B')  # Convert date to month name

# Optionally, rearrange columns if needed
InterestRate_Data_df = InterestRate_Data_df[['Year', 'Month', 'Rate']]

# Convert 'Rate' to float, handle non-numeric issues
InterestRate_Data_df['Rate'] = pd.to_numeric(InterestRate_Data_df['Rate'], errors='coerce')
InterestRate_Data_df["Year"] = InterestRate_Data_df["Year"].astype('str')

print(InterestRate_Data_df)