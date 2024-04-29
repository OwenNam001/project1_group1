# Common Module for Unemployment Rate data retrieval

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import bls_api_key

# Create a dataFrame for Monthly Unployment Rate

URL = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

api_key = bls_api_key
series_id = 'LNS14000000'  # Series ID for US unemployment rate
startyear = '2014'
endyear = '2019'

# Parameter setting
params = {
    'seriesid': series_id,
    'startyear':startyear,
    'endyear': endyear,
    'registrationKey': api_key
}

# Fetch unemployment data from BLS
response = requests.post(URL, json=params)
unemployment_data = response.json()


def get_unemployment_data():
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

    return unemployment_data_df