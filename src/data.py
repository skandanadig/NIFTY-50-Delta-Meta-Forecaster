import yfinance as yf
import pandas as pd
import os

def download_data(symbol, start, end, output_path):
    print(f"Downloading {symbol} data...")
    data = yf.download(symbol, start=start, end=end)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path)
    return data
