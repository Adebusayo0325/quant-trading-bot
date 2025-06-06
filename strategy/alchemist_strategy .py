# Basic placeholder Alchemist strategy

def get_signal(symbol, price):
    # Dummy logic: BUY if price ends with 5, else SELL
    if str(price).endswith("5"):
        return "BUY"
    else:
        return "SELL"
