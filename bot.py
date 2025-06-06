import time
from config import TRADE_SYMBOLS, ORDER_TYPE, TRADE_BALANCE, TAKE_PROFIT_PERCENT, STOP_LOSS_PERCENT
from exchange.binance_client import BinanceClient
from strategy.smc_strategy import get_signal as smc_signal
from strategy.alchemist_strategy import get_signal as alchemist_signal
from strategy.ict_strategy import get_signal as ict_signal
from signals.notifier import send_telegram_message
from utils.helpers import calculate_tp_sl

def aggregate_signals(symbol, price):
    signals = []
    signals.append(smc_signal(symbol, price))
    signals.append(alchemist_signal(symbol, price))
    signals.append(ict_signal(symbol, price))

    # Majority vote
    buy_count = signals.count("BUY")
    sell_count = signals.count("SELL")

    if buy_count > sell_count:
        return "BUY"
    elif sell_count > buy_count:
        return "SELL"
    else:
        return "HOLD"

def main():
    client = BinanceClient()

    while True:
        for symbol in TRADE_SYMBOLS:
            price = client.get_price(symbol)
            signal = aggregate_signals(symbol, price)

            if signal == "HOLD":
                continue

            quantity = round(TRADE_BALANCE / price, 6)
            take_profit, stop_loss = calculate_tp_sl(price, TAKE_PROFIT_PERCENT, STOP_LOSS_PERCENT, signal)

            order_response = client.place_order(
                symbol=symbol,
                side=signal,
                order_type=ORDER_TYPE,
                quantity=quantity,
                price=price  # Using current price as limit price for demo
            )

            message = (
                f"Trade Signal: *{signal}*\n"
                f"Symbol: {symbol}\n"
                f"Price: {price}\n"
                f"Quantity: {quantity}\n"
                f"Take Profit: {take_profit}\n"
                f"Stop Loss: {stop_loss}\n"
                f"Order Response: {order_response}"
            )
            send_telegram_message(message)
            print(message)

            time.sleep(10)  # To avoid rate limit

if __name__ == "__main__":
    main()
