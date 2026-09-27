import pytest
import numpy as np
from src.preprocessing import create_sliding_window

def test_create_sliding_window():
    data = np.arange(10)
    X, y = create_sliding_window(data, window_size=3)
    assert X.shape == (7, 3)
    assert y.shape == (7,)
    np.testing.assert_array_equal(X[0], [0, 1, 2])
    assert y[0] == 3
