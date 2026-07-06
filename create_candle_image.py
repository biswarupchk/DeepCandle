import pandas as pd
import mplfinance as mpf
from datetime import datetime

def create_candle_image(ohlc, path="latest.png"):
    df = pd.DataFrame([ohlc])
    df.index = [datetime.now()]
    
    mpf.plot(df, type='candle', style='charles', savefig=path)
    
    return path
