# DeepCandle

## AI-Powered Real-Time Candlestick Pattern Scanner

DeepCandle is a Python-based machine learning project that automatically detects bullish **Marubozu candlestick patterns** from live stock market data and sends instant Telegram alerts when a valid pattern is identified.

The project combines financial data collection, computer vision, deep learning, and automated notifications into a single real-time scanning pipeline.

---

## Features

- Real-time stock market scanning
- Automatic OHLC data collection
- Candlestick image generation
- CNN-based Marubozu pattern classification
- Instant Telegram notifications
- Modular and scalable Python architecture

---

## Project Workflow

1. Fetch live OHLC market data
2. Generate candlestick chart images
3. Load trained CNN model
4. Classify the candlestick pattern
5. Send Telegram alert if a Marubozu pattern is detected

---

## Tech Stack

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Yahoo Finance API
- Telegram Bot API

---

## Project Files

| File | Purpose |
|------|---------|
| main.py | Main program |
| fetch_ohlc.py | Downloads OHLC market data |
| create_candle_image.py | Creates candlestick chart images |
| classify.py | Predicts candlestick pattern using the trained CNN model |
| alert.py | Sends Telegram notifications |
| marubozu_model.h5 | Trained Deep Learning model |

---

## Model

The project uses a Convolutional Neural Network (CNN) trained to recognize bullish Marubozu candlestick patterns from generated candlestick images.

## Future Improvements

- Multi-pattern detection
- Support for additional candlestick formations
- Web dashboard
- Docker deployment
- Cloud deployment
- Live broker integration

## Disclaimer

This project was developed for educational and portfolio purposes and should not be considered financial advice.

## Author

**Biswarup Chakraborty**

Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer
