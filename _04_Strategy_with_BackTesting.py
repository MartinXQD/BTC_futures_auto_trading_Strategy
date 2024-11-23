
# Strategy based on the signal of futures price if exceed the upper&lower band
import numpy as np
from _02_Bollinger_Calculation import get_bollinger_data
https://github.com/MartinXQD/BTC_futures_auto_trading_Strategy/blob/Strategy-and-Performance-BackTesting/_04_Strategy_with_BackTesting.py
btc_df = get_bollinger_data()
# Determine Signal and Positions 
def determine_Long_Short(btc_df, periods=20, t=2.33):
    #Set Position to NAN 
    btc_df['position'] = np.nan
    #Set Postion to Buy and Long the futures 
    btc_df['position'] = np.where(
        btc_df['High'] >= btc_df['Upper'], 1, btc_df['position'])
    #Set Postion to Sell and Short the futures 
    btc_df['position'] = np.where(
        btc_df['Low'] <= btc_df['Lower'], -1, btc_df['position'])
'''
In this strategy, a signal change also indicates a closing of the current position (either take-profit or stop-loss) and simultaneously entering a reverse position (long or short) at the same time. 
I attempted to add a condition where, during a long position, if the price retraced to the moving average (SMA), the position would be closed, and similarly for a short position. 
Assuming the postion is Long, and the STOP-LOSS command should be  : 
                btc_df['position'] = np.where( (btc_df['position'] == 1) & (btc_df['Low'] <= btc_df['SMA']) & (btc_df['Low'] > btc_df['Lower']), 0, btc_df['position'])

However, the results showed a decrease in profitability. 
Through experimentation, I discovered that this is due to the lack of consideration for the continuous nature of price movements in each row of data. 
This causes a delay in executing stop-loss actions until the next candlestick, even if the price momentarily touched the SMA within the current candlestick. 
In actual trading, such a stop-loss mechanism would likely improve profitability，
especially since the current condition without a stop-loss has already endured greater drawdowns compared to the real-world scenario with stop-loss in place.
'''

    #Propagate the previous position forward until a new signal is generated
    btc_df['position'] = btc_df['position'].ffill()

    return returns(btc_df)


def returns(btc_df):

    btc_df['hrly_return'] = btc_df['Close'].pct_change(fill_method=None)
    btc_df['Cumulated_return'] = 0.0
    btc_df['Strategy_return'] = 0.0
    btc_df['compounded_return'] = 0.0
    btc_df['tradecount'] = 0
    btc_df['position'] = btc_df['position'].fillna(0)
    btc_df['hrly_return'] = btc_df['hrly_return'].fillna(0)
    btc_df['Continuosly_return'] = 10000.00

    btc_df['hold_change'] = 10000.00
    added = 0.0
    lastp = 0
    tradecount = 0
    initial = 10000.00
    for i in range(1, len(btc_df)):
        if btc_df['position'].iloc[i] != lastp:
            btc_df.loc[i-1, 'Strategy_return'] = added
            initial = initial * (1+btc_df.loc[i-1, 'Strategy_return'])
            added = btc_df['hrly_return'].iloc[i]*btc_df['position'].iloc[i]
            btc_df.loc[i, 'Cumulated_return'] = added
            btc_df.loc[i, 'Continuosly_return'] = initial * \
                (1+btc_df['hrly_return'].iloc[i]*btc_df['position'].iloc[i])
            lastp = btc_df['position'].iloc[i]
            tradecount += 1

        else:
            added += btc_df['hrly_return'].iloc[i]*btc_df['position'].iloc[i]
            btc_df.loc[i, 'Cumulated_return'] = added
            if btc_df['position'].iloc[i] != 0.0:
                btc_df.loc[i, 'Continuosly_return'] = btc_df.loc[i-1, 'Continuosly_return'] + initial * \
                    (btc_df['hrly_return'].iloc[i]
                     * btc_df['position'].iloc[i])

    for i in range(1, len(btc_df)):
        btc_df.loc[i, 'hold_change'] = btc_df.loc[i-1,
                                                  'hold_change']*(1+btc_df.loc[i, 'hrly_return'])
    btc_df['compounded_return'] = (1 + btc_df['Strategy_return']).cumprod() - 1
    last_index = btc_df.index[-2]
    btc_df.loc[last_index, 'tradecount'] = tradecount

    return btc_df


btc_df = determine_Long_Short(btc_df, periods=20, t=2.33)

btc_df = btc_df.drop(btc_df.index[-1])
