import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

#st.set_page_config(page_title="Correlation Dashboard", page_icon=":rocket:", layout = "wide")                 
                    
#import csv data and convert to pandas data frame
df_bayc = pd.read_csv (r'/Users/daltonnisbett/Documents/CODE/Project/Data/bayc-usd-max.csv')
df_punk = pd.read_csv (r'/Users/daltonnisbett/Documents/CODE/Project/Data/punk-usd-max.csv')
df_eth = pd.read_csv (r'/Users/daltonnisbett/Documents/CODE/Project/Data/eth-usd-max.csv')
df_btc = pd.read_csv (r'/Users/daltonnisbett/Documents/CODE/Project/Data/btc-usd-max.csv')
df_sol = pd.read_csv (r'/Users/daltonnisbett/Documents/CODE/Project/Data/sol-usd-max.csv')

#delete columns from dataframe
del df_bayc['market_cap']
del df_bayc['total_volume']
del df_punk['market_cap']
del df_punk['total_volume']
del df_eth['market_cap']
del df_eth['total_volume']
del df_btc['market_cap']
del df_btc['total_volume']
del df_sol['market_cap']
del df_sol['total_volume']

#rename columns in dataframe
df_bayc = df_bayc.rename(columns={'snapped_at': 'time', 'price': 'bayc_price'})
df_punk = df_punk.rename(columns={'snapped_at': 'time2', 'price': 'punk_price'})
df_eth = df_eth.rename(columns={'snapped_at': 'time3', 'price': 'eth_price'})
df_btc = df_btc.rename(columns={'snapped_at': 'time4', 'price': 'btc_price'})
df_sol = df_sol.rename(columns={'snapped_at': 'time5', 'price': 'sol_price'})

#change dataset
df_eth = df_eth.drop(range(0,2166))
df_eth = df_eth.reset_index()

df_btc = df_btc.drop(range(0,2995))
df_btc = df_btc.reset_index()

df_sol = df_sol.drop(range(0,458))
df_sol = df_sol.reset_index()

#merge prices dataframe
result = pd.concat([df_bayc, df_punk, df_eth, df_btc, df_sol], axis=1)
del result['time2']
del result['time3']
del result['time4']
del result['time5']
del result['index']

print(result)

#Bored Ape Yacht Club Correlation
print('BAYC - CRYPTOPUNKS: ', result.bayc_price.corr(result.punk_price))
print('BAYC - ETH: ', result.bayc_price.corr(result.eth_price))
print('BAYC - BTC: ', result.bayc_price.corr(result.btc_price))
print('BAYC - SOL: ', result.bayc_price.corr(result.sol_price))

#Crypto Punk Correlation
print('CRYPTOPUNKS - ETH: ', result.punk_price.corr(result.eth_price))
print('CRYPTOPUNKS - BTC: ', result.punk_price.corr(result.btc_price))
print('CRYPTOPUNKS - SOL: ', result.punk_price.corr(result.sol_price))

#Crypto Correlation 
BTCETH = result.btc_price.corr(result.eth_price)
BTCSOL = result.btc_price.corr(result.sol_price)
ETHSOL = result.eth_price.corr(result.sol_price)

#st.dataframe(result)

#side bar
