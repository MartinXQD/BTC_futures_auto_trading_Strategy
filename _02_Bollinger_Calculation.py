
#Construct Bollinger Bands for 1-hour candlestick charts.

import numpy as np
from _01_Import_Data_Frame import get_data

btc_df = get_data()
# Bollinger Band with 𝑡=2.33， corresponding to a 1% extreme scenario under the assumption of a normal distribution
def BollingerBand(btc_df, periods=20, t=2.33):
    #  Define column names for Bollinger Band construction
    key = ['Upper', 'Lower', 'STDEV', 'TyP', 'SMA']
    ub, lb, stdev, price, sma_20 = key
    #Calculate the Typical Price for each entry
    btc_df[price] = btc_df.apply(lambda x: np.mean(
        x[['High', 'Low', 'Close']]), axis=1)
    
    btc_df[sma_20] = btc_df[price].rolling(periods).mean()
    btc_df[stdev] = btc_df[price].rolling(periods).std()
    btc_df[ub] = btc_df[sma_20] + t * btc_df[stdev]
    btc_df[lb] = btc_df[sma_20] - t * btc_df[stdev]

    return btc_df


def get_bollinger_data():

    return BollingerBand(btc_df)


# Visualizaiton
#btc_df = get_bollinger_data()
# print(btc_df.iloc[30:40])
