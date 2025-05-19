from okx import Trade
from Application_01_Config import api_key, secret_key, passphrase, IS_SIMULATION

tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase,
                          False, flag="1" if IS_SIMULATION else "0")


def place_order(instId, position, size="1"):
    if position == 0:
        print("No action this hour.")
        return

    side = "buy" if position == 1 else "sell"
    try:
        result = tradeAPI.place_order(
            instId=instId,
            tdMode="cross",
            side=side,
            ordType="market",
            sz=size
        )
        print(f"Order placed: {side} {size} {instId} → {result}")
    except Exception as e:
        print(f"Failed to place order: {e}")
