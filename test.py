import requests
import pandas as pd
import yfinance as yf
#Test a strategy

#Create index_rebalancing class

#For Loop,
#Every minute
#Get price of index
#Get price of components + weighting to create a synthetic index
#If price of index > components, sell (short) the index and buy the synthetic index
#IF price of index < components, buy the index and sell (short) the synthetic index
#Record positions and pnl

#This strategy is an arbitrage strategy that profits from discrepancies between the price of an index and its components
#We will backtest on the Bitwise 10 (top 10 cryptos) pricing data 

BITW = yf.Ticker("BITW")
index_data = BITW.history(period="3mo")

cryptos = ["BTC-USD","ETH-USD","SOL-USD","XRP-USD","ADA-USD","AVAX-USD",
           "LINK-USD", "BCH-USD", "DOT-USD", "UNI7083-USD"]

crypto_data = {}

for crypto in cryptos:
    ticker = yf.Ticker(crypto)
    crypto_data[crypto] = ticker.history(period="3mo")
    
print(crypto_data)







#while True:
#   IndexPrice = 