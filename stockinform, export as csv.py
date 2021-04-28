import yfinance as yf
import pandas as pd

stock = yf.download('AAPL', period = '5y')      #You can change the stock name to any stock you want to view, and the period too

print('Total length of the stock data:', len(stock))

print(stock.head())
print(stock.tail())

stock.info()

stock.to_csv('msft.csv')        #export the data as csv and save to your machine