import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

def scale_data(data, scaler_type='MinMax'):
    if scaler_type == 'MinMax':
        scaler = MinMaxScaler()
    elif scaler_type == 'Standard':
        scaler = StandardScaler()
    else:
        scaler = RobustScaler()
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    return scaled, scaler

def create_sliding_window(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)
