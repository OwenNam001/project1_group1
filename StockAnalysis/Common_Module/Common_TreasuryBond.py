# Common Module to aquire info from FRED API, used for Interest Rates, 

# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import fred_api_key


def get_year2BondRate_Data_data():

    # FRED API url assembly
    url = "https://api.stlouisfed.org/fred/series/observations"
    year2Bondparams = {
        "series_id": "DGS2",  # Series ID for the US 2-Year Treasury Bond Rate
        "api_key": fred_api_key,  # Replace with your API key
        "file_type": "json",
        "observation_start": "2010-01-01", # Starting year of data gathering
        "observation_end": "2019-12-31" 
    }
    # Fetching the request
    response_data = requests.get(url, params=year2Bondparams).json()

    ## FRED API dataframe
    datatotal = 0
    updated_date = []
    updated_rate = [] # assigned variables outside forloop with empty variables ready to be appended
    # For loop will take the date and rate from the json file for the 10 years requested and add the values to a new array
    for observation in response_data["observations"]:
        date = observation["date"]
        year2bond_rate = observation["value"]
        updated_date.append(date)
        updated_rate.append(year2bond_rate)
        datatotal = datatotal + 1

    Year2BondRate_Data_df = pd.DataFrame({
        "Date" : updated_date,
        "Year2Bond_Rate" : updated_rate
        })
    Year2BondRate_Data_df[['Year', 'Month', 'Day']] = Year2BondRate_Data_df["Date"].str.split('-', expand=True)
    Year2BondRate_Data_df["Month"] = Year2BondRate_Data_df['Month'].astype(float) # year and month both needed to change to float for the merge

    # Data Cleanding - Drop all rows with missing information
    Year2BondRate_Data_df = Year2BondRate_Data_df.dropna(how='any')

    return Year2BondRate_Data_df


def get_year10BondRate_Data_data():

    # FRED API url assembly
    url = "https://api.stlouisfed.org/fred/series/observations"
    year10Bondparams = {
        "series_id": "DGS10",  # Series ID for the US 10-Year Treasury Bond Rate
        "api_key": fred_api_key,  # Replace with your API key
        "file_type": "json",
        "observation_start": "2010-01-01", # Starting year of data gathering
        "observation_end": "2019-12-31" 
    }
    # Fetching the request
    response_data = requests.get(url, params=year10Bondparams).json()

    ## FRED API dataframe
    datatotal = 0
    updated_date = []
    updated_rate = [] # assigned variables outside forloop with empty variables ready to be appended
    # For loop will take the date and rate from the json file for the 10 years requested and add the values to a new array
    for observation in response_data["observations"]:
        date = observation["date"]
        year10bond_rate = observation["value"]
        updated_date.append(date)
        updated_rate.append(year10bond_rate)
        datatotal = datatotal + 1

    Year10BondRate_Data_df = pd.DataFrame({
        "Date" : updated_date,
        "Year10Bond_Rate" : updated_rate
        })
    Year10BondRate_Data_df[['Year', 'Month', 'Day']] = Year10BondRate_Data_df["Date"].str.split('-', expand=True)
    Year10BondRate_Data_df["Month"] = Year10BondRate_Data_df['Month'].astype(float) # year and month both needed to change to float for the merge
    return Year10BondRate_Data_df