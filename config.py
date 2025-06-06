import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BASE_URL = os.getenv("BASE_URL", "https://testnet.binance.vision")
TRADE_SYMBOLS = os.getenv("TRADE_SYMBOLS", "BTCUSDT").split(",")
ORDER_TYPE = os.getenv("ORDER_TYPE", "LIMIT")

TRADE_BALANCE = float(os.getenv("TRADE_BALANCE", 10))
TAKE_PROFIT_PERCENT = float(os.getenv("TAKE_PROFIT_PERCENT", 1.5))
STOP_LOSS_PERCENT = float(os.getenv("STOP_LOSS_PERCENT", 0.5))
