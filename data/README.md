# NIFTY-50 Dataset

This directory contains the dataset used for the NIFTY-50 index forecasting models.

## Source
The historical NIFTY-50 OHLC (Open, High, Low, Close) data is sourced from **Yahoo Finance**.

## Date Range
- **Start Date:** January 1, 2013
- **End Date:** January 1, 2024 (11-year period)

## Features (Columns)
- `Date`: Trading date
- `Open`: Opening price of the index
- `High`: Highest price of the index during the trading day
- `Low`: Lowest price of the index during the trading day
- `Close`: Closing price of the index (used as the base for the target variable)
- `Adj Close`: Adjusted closing price (optional)
- `Volume`: Trading volume (optional depending on usage, but paper relies mainly on OHLC)

## How to Obtain
You can fetch this data directly using the `yfinance` Python library:

```python
import yfinance as yf

# Download NIFTY 50 data
nifty_data = yf.download('^NSEI', start='2013-01-01', end='2024-01-01')
nifty_data.to_csv('nifty50_2013_2024.csv')
```

## Preprocessing Details
- The data is restructured using a **10-day sliding window** approach (p=10).
- The target variable is the next day's closing price ($y_{t+1}$).
- The dataset is partitioned chronologically into Training (60%), Validation (15%), and Testing (25%) without shuffling to prevent data leakage.
- Scaling techniques evaluated include Min-Max, Standard, and Robust scalers.
