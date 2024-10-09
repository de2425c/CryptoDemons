from pycoingecko import CoinGeckoAPI
import requests
import pandas as pd

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