from _02_Bollinger_Calculation import get_bollinger_data
from _04_Strategy import determine_Long_Short
btc_df = get_bollinger_data()
btc_df = determine_Long_Short(btc_df)


def alpha_calculation(btc_df):
    # the total compound return at the end
    last_return = btc_df['compounded_return'].iloc[-1]
    price_change = (btc_df['Open'].iloc[-1] - btc_df['Open'].iloc[1]) / \
        btc_df['Open'].iloc[1]  # the price change for hold to the end
    alpha = last_return - price_change
    return alpha


def maximum_drawdown(btc_df):
    peak = btc_df['Continuosly_return'].cummax()
    drawdown = (peak - btc_df['Continuosly_return'])/peak
    max_drawdown = drawdown.max()
    return max_drawdown


alpha = alpha_calculation(btc_df)
max_drawdown = maximum_drawdown(btc_df)
print(f"Alpha: {alpha * 100}%")
print(f"Maximum Drawdown: {max_drawdown: .2%}")
