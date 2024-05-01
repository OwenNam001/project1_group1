# project1_group1 (DUE DATE : 6th of May)

## Title : Exploring Correlations in the Stock Market

## Team Members : Jun Nam, Yau Shu Wong, Bailey, Rekha

## Working file name should be yourname suffix to prevent conflict, Will make naming convention

## Project Description / Outline  

- We will explore to identify the correlations between various macroeconomic indicators and US stock prices

<< Stock Profits vs Month >>
- Monthly Profits over 10 years. month (x-axis) (correlation between price and Month) (Jun) **01.Yearly_Monthly_Profits.ipynb**

<< Stock Profits vs US Presidential election year or normal year >>
- Yearly profits (y-axis) for year (x-axis) presidential election year (red dot), non presidential election year by (blue dot) (Rekha) **02.Yearly_Profits_Election.ipynb**

<< Stock Profits vs unemployeement >>
- Monthly profits [one month before unemployeement announce] (y-axis) vs unemployeement rate (x-axis) (Yau Shu) **03.Monthly_Profits_Unemploy_1Mago.ipynb**
- Monthly profits [same month with unemployeement announce] (y-axis) vs unemployeement rate (x-axis) (Yau Shu) **04.Monthly_Profits_Unemploy_M.ipynb**
- Monthly profits [one month after unemployeement announce] (y-axis) vs unemployeement rate (x-axis) (Yau Shu) **05.Monthly_Profits_Unemploy_1Mafter.ipynb**
- Monthly closing Stock price and unemployeement rate (y-axis), Year, Month combined (x-axis) for 10 years (Jun) **06.Monthly_Closing_Unemploy.ipynb**

<< Stock Profits vs Interest rate >>
- Monthly profits [one month before interest rate announce] (y-axis) vs interest rate (x-axis) (Bailey) **07.Monthly_Profits_Fundrate_1Mago.ipynb**
- Monthly profits [same month with interest rate announce] (y-axis) vs interest rate (x-axis) (Bailey) **08.Monthly_Profits_Fundrate_M.ipynb**
- Monthly profits [one month after interest rate announce] (y-axis) vs interest rate (x-axis) (Bailey) **09.Monthly_Profits_Fundrate_1Mafter.ipynb**
- Monthly closing Stock price and Interest rate (y-axis), Year, Month combined (x-axis) for 10 years (Jun) **10.Monthly_Closing_Fundrate.ipynb**

<< Stock Profits vs US Bond rate>>
- Monthly profits (y-axis) vs 2 year US Bond Monthly rate change (x-axis) (Jun) **11.Monthly_Profits_2YearBond.ipynb**
- Monthly profits (y-axis) vs 10 year US Bond Monthly rate change (x-axis) (Jun) **12.Monthly_Profits_10YearBond.ipynb**
- Monthly closing Stock price and 2, 10 year US Bond rate Year, Month combined (x-axis) for 10 years (Jun) **13.Monthly_Closing_Bond.ipynb**

<< Stock Profits vs US Dollar index >>
- Monthly profits (y-axis) vs Monthly dollar index change (x-axis) (Yau Shu)
- Daily closing Stock price and US Dollar index (y-axis : scaling 0 ~ 1), Daily (x-axis) for 10 years by line plot (Bailey)

<< Stock Profits vs US Volatility index (VIX) >>
- Daily profits (y-axis) vs Daily VIX index change (x-axis) by scatter plot using Alphavantage API (Yau Shu)
- Daily closing Stock price and VIX index (y-axis : scaling 0 ~ 1), Daily (x-axis) for 10 years by line plot (Bailey)

<< Stock Profits vs Gold Price, BITCOIN >>
- Monthly profits (y-axis) vs Monthly Gold Price change (x-axis) by scatter plot using Alphavantage API (Rekha)
- Monthly profits (y-axis) vs Monthly BITCOIN Price change (x-axis) by scatter plot using Alphavantage API (Rekha)

## Datasets to Be Used
- https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.json?start_date=1985-05-01&end_date=1997-07-01&order=asc&column_index=4&collapse=quarterly&transformation=rdiff
- BLS (U.S Bureau of Labor Statistics) API : https://www.bls.gov/developers/
- FRED (economic) API : https://fred.stlouisfed.org/docs/api/fred/
- Fiscaldata treasury : https://fiscaldata.treasury.gov/api-documentation
- Alphavantage API : https://www.alphavantage.co/documentation/

## Breakdown of Tasks
- Each members will take 5 tasks 
