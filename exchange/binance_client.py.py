import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import BINANCE_API_KEY, BINANCE_API_SECRET, BASE_URL

class BinanceClient:
    def __init__(self):
        self.api_key = BINANCE_API_KEY
        self.api_secret = BINANCE_API_SECRET
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({'X-MBX-APIKEY': self.api_key})

    def _sign_payload(self, params):
        query_string = urlencode(params)
        signature = hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        return signature

    def place_order(self, symbol, side, order_type, quantity, price=None):
        url = f"{self.base_url}/api/v3/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign_payload(params)
        response = self.session.post(url, params=params)
        return response.json()

    def get_price(self, symbol):
        url = f"{self.base_url}/api/v3/ticker/price"
        params = {"symbol": symbol}
        response = self.session.get(url, params=params)
        data = response.json()
        return float(data.get("price", 0))
