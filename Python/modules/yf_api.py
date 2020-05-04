# Read stock infor from Yahoo finance API

import json
import yfinance as yf

# Access ticker data

msft = yf.Ticker("MSFT")

info = msft.info
print(info.keys())

hist = msft.history(period='max')
print('\n History: \n', hist)

print('\n Actions: \n', msft.actions)

print('\n Dividends: \n', msft.dividends)

print('\n Major holders: \n', msft.major_holders)

print('\n Instituitional holders: \n', msft.institutional_holders)

print('\n Cash flow: \n', msft.cashflow)

print('\n Analysts recommendations: \n', msft.recommendations)

# Initialise multiple Ticker objects

tickers = yf.Tickers('TSLA AAPL GOOG')

print(dir(tickers.tickers))
print('\n AAPL history: \n', tickers.tickers.AAPL.history(period='max'))
print('\n GOOG actions: \n', tickers.tickers.GOOG.actions)
print('\n TSLA dividends: \n', tickers.tickers.TSLA.dividends)

# Fetching data for multiple tickers

data = yf.download(tickers="SPY AAPL", period='10y', interval='1d',
                   group_by='ticker', auto_adjust=True)

print(data.head())

# Override pandas_datareader

from pandas_datareader import data as pdr

yf.pdr_override()
hijacked = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2018-01-01")

print(hijacked.head())