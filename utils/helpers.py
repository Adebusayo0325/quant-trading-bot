def calculate_tp_sl(price, take_profit_percent, stop_loss_percent, side):
    if side == "BUY":
        take_profit = price * (1 + take_profit_percent / 100)
        stop_loss = price * (1 - stop_loss_percent / 100)
    else:
        take_profit = price * (1 - take_profit_percent / 100)
        stop_loss = price * (1 + stop_loss_percent / 100)
    return round(take_profit, 8), round(stop_loss, 8)
