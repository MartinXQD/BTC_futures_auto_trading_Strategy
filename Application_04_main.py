
import time
from Application_02_strategy import fetch_klines, generate_signal
from Application_03_trade_executor import place_order


def run_strategy():
    df = fetch_klines()
    signal = generate_signal(df)
    print(f"Signal = {signal}")
    place_order("BTC-USDT-SWAP", signal)


if __name__ == "__main__":
    while True:
        run_strategy()
        time.sleep(60 * 60)  # for each hr
