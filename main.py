import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fetch_ohlc import get_btc_5m
from create_candle_image import create_candle_image
from classify import load_marubozu_model, predict
from telegram.alert import send_alert
from config import MODEL_PATH, THRESHOLD
import time

def run_scanner():
    print("Loading model...")
    model = load_marubozu_model(MODEL_PATH)
    print("Model loaded!")

    while True:
        print("Fetching BTC 5-minute candle...")
        ohlc = get_btc_5m()

        print("Creating candle image...")
        img = create_candle_image(ohlc)

        print("Classifying...")
        prob, is_marubozu = predict(model, img, THRESHOLD)

        print(f"Probability={prob:.4f} | Marubozu={is_marubozu}")

        if is_marubozu:
            send_alert(f" Marubozu Detected!\nProbability: {prob:.4f}")

        print("Waiting 5 minutes...\n")
        time.sleep(300)

if __name__ == "__main__":
    run_scanner()
