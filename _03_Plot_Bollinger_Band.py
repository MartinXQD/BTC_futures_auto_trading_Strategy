
# Visualize dataframe with Bollinger band. 
import mplfinance as mpf
from _02_Bollinger_Calculation import get_bollinger_data

btc_df = get_bollinger_data()

def plot_bollinger_band(btc_df):
    # Replace time with indexes for tracking
    btc_df.set_index('Time', inplace=True)
    # plot Bollinger Band
    apdict = mpf.make_addplot(btc_df[['SMA', 'Upper', 'Lower']])
    # Visualize BTC/USDT Futures 1-H K line
    mpf.plot(btc_df, type='candle', addplot=apdict, title='BTCUSDT Futures Price with Bollinger Bands',
             ylabel='Price', volume=False)


plot_bollinger_band(btc_df)
