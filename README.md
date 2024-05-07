# project1_group1

## Title : Exploring Correlations in the Stock Market

## Team Members : Jun Nam, Yau Shu Wong, Bailey, Rekha

## Project Description / Outline  

- We will explore to identify the correlations between various macroeconomic indicators and US stock prices

<< Stock Profits vs Month >>
- Monthly Profits over 10 years. month (x-axis) (correlation between price and Month) **01.Yearly_Monthly_Profits.ipynb**

<< Stock Profits vs unemployeement >>
- Monthly profits [one month before unemployeement announce] (y-axis) vs unemployeement rate (x-axis) **02.Monthly_Profits_Unemploy_1Mago.ipynb**
- Monthly profits [same month with unemployeement announce] (y-axis) vs unemployeement rate (x-axis) **03.Monthly_Profits_Unemploy_M.ipynb**
- Monthly profits [one month after unemployeement announce] (y-axis) vs unemployeement rate (x-axis) **04.Monthly_Profits_Unemploy_1Mafter.ipynb**
- Monthly closing Stock price and unemployeement rate (y-axis), Year, Month combined (x-axis) for 10 years **05.Monthly_Closing_Unemploy.ipynb**

<< Stock Profits vs Interest rate >>
- Monthly profits [one month before interest rate announce] (y-axis) vs interest rate (x-axis) **06.Monthly_Profits_Fundrate_1Mago.ipynb**
- Monthly profits [same month with interest rate announce] (y-axis) vs interest rate (x-axis) **07.Monthly_Profits_Fundrate_M.ipynb**
- Monthly profits [one month after interest rate announce] (y-axis) vs interest rate (x-axis) **08.Monthly_Profits_Fundrate_1Mafter.ipynb**
- Monthly closing Stock price and Interest rate (y-axis), Year, Month combined (x-axis) for 10 years **09.Monthly_Closing_Fundrate.ipynb**

<< Stock Profits vs US Bond rate>>
- Monthly profits (y-axis) vs 2 year US Bond Monthly rate change (x-axis) **10.Monthly_Profits_2YearBond.ipynb**
- Monthly profits (y-axis) vs 10 year US Bond Monthly rate change (x-axis) **11.Monthly_Profits_10YearBond.ipynb**
- Monthly closing Stock price and 2, 10 year US Bond rate Year, Month combined (x-axis) for 10 years **12.Monthly_Closing_Bond.ipynb**

<< Stock Profits vs US Real GDP per Capita >>
- Monthly profits (y-axis) vs Quarterly Real GDP per Capita (x-axis) by scatter plot using Alphavantage API **13.Monthly_Profits_GDP.ipynb**
- Daily closing Stock price and US Real GDP per Capita Daily (x-axis) for 10 years by line plot **14.Daily_Closing_vs_RealGDP.ipynb**

<< Stock Profits vs US CPI >>
- Monthly profits (y-axis) vs Monthly US CPI (x-axis) by scatter plot using Alphavantage API **15.Monthly_Profits_CPI.ipynb**
- Daily closing Stock price and US CPI Daily (x-axis) for 10 years by line plot **16.Daily_Closing_vs_US_CPI.ipynb**

## Datasets to Be Used
- BLS (U.S Bureau of Labor Statistics) API : https://www.bls.gov/developers/
- FRED (economic) API : https://fred.stlouisfed.org/docs/api/fred/
- Alphavantage API : https://www.alphavantage.co/documentation/

## Breakdown of Tasks
- Each members will take 5 tasks 

## Conclusions
- Purchasing stock in end of May, will yield a probability of the stock profit at the end of June of ~70%.
- Do not recommend to trade Stock in July as this is the worst performing month on average over 10-year.
- The monthly stock profit does not appear to show any correlation with the unemployment rate
- The stock closing price and unemployment rate is showing an opposite trend over time
- It does appear to have any correlation between the monthly stock profit and Federal Interest Rates
- The monthly closing price vs interest rate over time appears to differ between pre & post 2016.
- Stock price in 2-years US Treasury Bond Rate is showing similar trend over time. However, there are no correlation between the stock price and the 10-year Treasury Bond Rate.
- The monthly stock profit does not appear to show any correlation with the Quarterly GDP per Capita.
- The closing stock price vs GDP has a correlation value of 0.99.
- The monthly stock profit does not appear to show any correlation with the CPI.
- The closing stock price vs CPI has a correlation value of 0.97.