# Common Module to aquire info from FRED API, used for Interest Rates, 

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import fred_api_key

# FRED API url assembly
url = "https://api.stlouisfed.org/fred/series/observations"
FEDFUNDparams = {
    "series_id": "FEDFUNDS",  # Interest rate series ID
    "api_key": fred_api_key,  # Replace with your API key
    "file_type": "json",
    "observation_start": "2010-01-01", # Starting year of data gathering
    "observation_end": "2019-12-31" 
}
# Fetching the request
response_data = requests.get(url, params=FEDFUNDparams).json()

def get_interest_data():
    ## FRED API dataframe
    datatotal = 0
    updated_date = []
    updated_rate = [] # assigned variables outside forloop with empty variables ready to be appended
    # For loop will take the date and rate from the json file for the 10 years requested and add the values to a new array
    for observation in response_data["observations"]:
        date = observation["date"]
        interest_rate = observation["value"]
        updated_date.append(date)
        updated_rate.append(interest_rate)
        datatotal = datatotal + 1

    monthly_interest_df = pd.DataFrame({
        "Date" : updated_date,
        "Interest_Rate" : updated_rate
        })
    monthly_interest_df[['Year', 'Month', 'Day']] = monthly_interest_df["Date"].str.split('-', expand=True)
    monthly_interest_df["Month"] = monthly_interest_df['Month'].astype(float) # year and month both needed to change to float for the merge

    # Data Cleanding - Drop all rows with missing information
    monthly_interest_df = monthly_interest_df.dropna(how='any')

    return monthly_interest_df
