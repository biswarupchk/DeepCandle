import requests

def get_btc_5m():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=1"
    data = requests.get(url).json()[0]

    ohlc = {
        "Open": float(data[1]),
        "High": float(data[2]),
        "Low": float(data[3]),
        "Close": float(data[4])
    }

    return ohlc
