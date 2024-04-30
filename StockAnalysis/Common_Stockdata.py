# Common Module for Stock price data retrieval

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import alpha_vantage_api_key


# Constants
stock_symbol = 'QQQ'
start_date = '2010-01-01'
end_date = '2019-12-31'

URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={alpha_vantage_api_key}&outputsize=full'


# Fetch stock data from alphavantage
response = requests.get(URL).json()

def get_stock_data():
    try:
        # Define an empty list to fetch the stock data
        stock_data = []

        for date, values in response['Time Series (Daily)'].items():
            stock_data.append({
                "Date": date,
                "Open": values['1. open'],
                "High": values['2. high'],
                "Low": values['3. low'],
                "Close": values['4. close'],
                "Volume": values['5. volume']
            })

        # Conver List to dataFrame
        stock_info_df = pd.DataFrame(stock_data)
        stock_info_df = stock_info_df[(stock_info_df['Date'] >= start_date) & (stock_info_df['Date'] <= end_date)]

        stock_info_df.reset_index()
        stock_info_df['Date'] = pd.to_datetime(stock_info_df['Date'])
        stock_info_df['Open'] = stock_info_df['Open'].astype(float)
        stock_info_df['Close'] = stock_info_df['Close'].astype(float)


        # Date, Month Column creation by using Date
        stock_info_df['Year'] = stock_info_df['Date'].dt.year

        stock_info_df['Month_Number'] = stock_info_df['Date'].dt.month

        return stock_info_df
    
    except KeyError as e:
        print(f"Key error: {e} - Check Response dictionary or data keys.")
        return None
    except ValueError as e:
        print(f"Value error: {e} - Check Data types and conversions.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None    



def get_stock_long_data():
    try:
        # Define an empty list to fetch the stock data
        stock_data = []

        for date, values in response['Time Series (Daily)'].items():
            stock_data.append({
                "Date": date,
                "Open": values['1. open'],
                "High": values['2. high'],
                "Low": values['3. low'],
                "Close": values['4. close'],
                "Volume": values['5. volume']
            })

        # Conver List to dataFrame
        stock_info_df = pd.DataFrame(stock_data)    

        stock_info_df.reset_index()
        stock_info_df['Date'] = pd.to_datetime(stock_info_df['Date'])
        stock_info_df['Open'] = stock_info_df['Open'].astype(float)
        stock_info_df['Close'] = stock_info_df['Close'].astype(float)


        # Date, Month Column creation by using Date
        stock_info_df['Year'] = stock_info_df['Date'].dt.year

        stock_info_df['Month_Number'] = stock_info_df['Date'].dt.month

        return get_stock_long_data
        except KeyError as e:
        print(f"Key error: {e} - Check Response dictionary or data keys.")
        return None
    except ValueError as e:
        print(f"Value error: {e} - Check Data types and conversions.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None    