
import mplfinance as mpf

from _02_Bollinger_Calculation import get_bollinger_data

btc_df = get_bollinger_data()

# plot Bollinger Band

def plot_bollinger_band(btc_df):
    btc_df.set_index('Time', inplace=True)

    apdict = mpf.make_addplot(btc_df[['SMA', 'Upper', 'Lower']])

    mpf.plot(btc_df, type='candle', addplot=apdict, title='BTC Price with Bollinger Bands',
             ylabel='Price', volume=False)


plot_bollinger_band(btc_df)
