# Basic placeholder Smart Money Concepts strategy

def get_signal(symbol, price):
    # Dummy logic: BUY if last digit of price is even, else SELL
    last_digit = int(str(price).split(".")[0][-1])
    if last_digit % 2 == 0:
        return "BUY"
    else:
        return "SELL"
