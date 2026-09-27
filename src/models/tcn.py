from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Dense, Dropout, Flatten

def build_tcn(input_shape):
    model = Sequential([
        Conv1D(filters=64, kernel_size=3, padding='causal', dilation_rate=1, activation='relu', input_shape=input_shape),
        Dropout(0.1),
        Conv1D(filters=64, kernel_size=3, padding='causal', dilation_rate=2, activation='relu'),
        Dropout(0.1),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
