# Common Module for Unemployment Rate data retrieval

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import bls_api_key

# Create a dataFrame for Monthly Unployment Rate

base_url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# Set parameters
seriesid = 'LNS14000000'
startyear = 2010
endyear = 2019
registrationkey = bls_api_key

# Parameter setting
params = {'seriesid':[seriesid],
          'startyear':startyear,
          'endyear':endyear,
          'registrationkey':registrationkey}

# Fetch unemployment data from BLS
response = requests.post(base_url, json=params)
unemployment_data = response.json()


def get_unemployment_data():
    
    try:

    # Initialize an empty list to hold the unemployment data
        unemployment_list = []

        # Extract data from the response
        series_data = unemployment_data["Results"]["series"][0]["data"]
        for item in series_data:
            unemployment_list.append({
                                        "Year": item["year"],
                                        "Month": item["periodName"],
                                        "Rate": item["value"]
                                    })

        # Convert the list to a DataFrame
        unemployment_data_df = pd.DataFrame(unemployment_list).reset_index(drop=True)
        unemployment_data_df["Rate"] = unemployment_data_df["Rate"].astype('float')
        unemployment_data_df['Year'] = unemployment_data_df['Year'].astype(object)
        unemployment_data_df['Month'] = unemployment_data_df['Month'].astype(object)

        return unemployment_data_df
    
    except KeyError as e:
        print(f"Key error: {e} - Check Response dictionary or data keys.")
        return None
    except ValueError as e:
        print(f"Value error: {e} - Check Data types and conversions.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  