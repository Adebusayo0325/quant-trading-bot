# Basic placeholder ICT (Inner Circle Trader) strategy

def get_signal(symbol, price):
    # Dummy logic: BUY if price above 100, SELL otherwise
    if price > 100:
        return "BUY"
    else:
        return "SELL"
