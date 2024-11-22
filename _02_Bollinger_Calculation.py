

import numpy as np
from _01_Data import get_data

btc_df = get_data()

# Calculate Bolliner Band


def BollingerBand(btc_df, periods=20, t=2.33):
    key = ['Upper', 'Lower', 'STDEV', 'TyP', 'SMA']
    ub, lb, stdev, price, sma_20 = key

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
