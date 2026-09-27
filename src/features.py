import numpy as np

def delta_transform(y_true, y_prev):
    '''Transform absolute prices to price changes (deltas)'''
    return y_true - y_prev

def inverse_delta_transform(delta, y_prev):
    '''Reconstruct absolute prices from deltas'''
    return y_prev + delta
