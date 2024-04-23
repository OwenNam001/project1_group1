# project1_group1

## Title : Exploring Correlations in the Stock Market

## Team Members : Jun Nam, Yau Shu Wong, Bailey, Rekha

## Project Description / Outline  
1. Outline projects ideas
- We will analyze the US Stock price
- We will trying to find any metrics (any nytimes API finding things with company name) that would be correlated to close price for a particular stock. apply linear regression, use Pearson Correlation method

- Monthly profits average (10 years) for each month (correlation between price and Month) by bar chart
- Yearly profits (y-axis) for year (x-axis) presidential election year (red dot), non presidential election year by blue dot by scatter plot

<< Stock Profits vs unemployeement >>
- Monthly profits [one month before unemployeement announce] (y-axis) vs unemployeement rate (x-axis) by scatter plot using BLS API
- Monthly profits [same month with unemployeement announce] (y-axis) vs unemployeement rate (x-axis) by scatter plot using BLS API
- Monthly profits [one month after unemployeement announce] (y-axis) vs unemployeement rate (x-axis) by scatter plot using BLS API

<< Stock Profits vs Interest rate >>
- Monthly profits [one month before interest rate announce] (y-axis) vs interest rate (x-axis) by scatter plot using FRED API
- Monthly profits [same month with interest rate announce] (y-axis) vs interest rate (x-axis) by scatter plot using FRED API
- Monthly profits [one month after interest rate announce] (y-axis) vs interest rate (x-axis) by scatter plot using FRED API


## Datasets to Be Used
- https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.json?start_date=1985-05-01&end_date=1997-07-01&order=asc&column_index=4&collapse=quarterly&transformation=rdiff
- BLS (U.S Bureau of Labor Statistics) API : https://www.bls.gov/developers/
- FRED (economic) API : https://fred.stlouisfed.org/docs/api/fred/

## Breakdown of Tasks
- Each members will take 2 tasks 
