# Dependencies and Setup
import requests
from pprint import pprint
import pandas as pd

# Import the API key
from api_keys import bls_api_key

# Create a dataFrame for Monthly Unployment Rate

URL = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

test_params = {
    'seriesid': 'LNS14000000',
    'startyear': 2010,
    'endyear': 2019,
    'registrationKey': '9477ce63175a4c2bacfe451a1e65d3fb'
}
test_response = requests.get(URL, test_params)
print(test_response.json())