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
index_data = BITW.history(period="5d", interval="1m")
index_data.index = pd.to_datetime(index_data.index).tz_convert('UTC')
cryptos = ["BTC-USD","ETH-USD","SOL-USD","XRP-USD","ADA-USD","AVAX-USD",
           "LINK-USD", "BCH-USD", "DOT-USD", "UNI7083-USD"]

crypto_data = {}

for crypto in cryptos:
    ticker = yf.Ticker(crypto)
    data = ticker.history(period="5d", interval="1m").tz_convert('UTC')
    data.index = pd.to_datetime(data.index)
    aligned_data = data.loc[data.index.intersection(index_data.index)]
    crypto_data[crypto] = aligned_data
 

indexdates = index_data.index
cryptodates = crypto_data["BTC-USD"].index
i = 0


weights = [.737,.176,.04,.018,.007,.006,.004,.004,.003,.003]

while i < len(indexdates):
    index_date = indexdates[i]
    index_price = index_data.loc[index_date, 'Open']
    
    crypto_date = cryptodates[i]
    crypto_prices = []
    for crypto in crypto_data:
        crypto_prices.append(crypto_data[crypto].loc[crypto_date,'Open'])
    
    j = 0
    for weight in weights:
        crypto_prices[j] = crypto_prices[0]*weight
        j+=1
    synthetic_index_price = sum(crypto_prices)
    
    print(synthetic_index_price)
    
    i+=1

    
    