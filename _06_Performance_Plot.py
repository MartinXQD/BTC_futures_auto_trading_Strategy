import mplfinance as mpf

from _04_Strategy import determine_Long_Short
from _02_Bollinger_Calculation import get_bollinger_data

btc_df = get_bollinger_data()
btc_df = determine_Long_Short(btc_df, periods=20, t=2.33)


def plot_investment_return(btc_df):

    btc_df.set_index('Time', inplace=True)
    apdict1 = mpf.make_addplot(
        btc_df[['Continuosly_return']], color='blue', title='real time position amount', ylabel='real time position amount',)
    apdict2 = mpf.make_addplot(btc_df[['hold_change']], color='orange',
                               )

    mpf.plot(btc_df, type='candle', addplot=[apdict1, apdict2],  title='BTC Price 1_h K',
             ylabel='Price', volume=False)


plot_investment_return(btc_df)
