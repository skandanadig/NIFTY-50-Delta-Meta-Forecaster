import pytest
import numpy as np
from src.features import delta_transform, inverse_delta_transform

def test_delta_transform():
    y_true = np.array([105, 110, 108])
    y_prev = np.array([100, 105, 110])
    expected = np.array([5, 5, -2])
    np.testing.assert_array_equal(delta_transform(y_true, y_prev), expected)

def test_inverse_delta_transform():
    delta = np.array([5, 5, -2])
    y_prev = np.array([100, 105, 110])
    expected = np.array([105, 110, 108])
    np.testing.assert_array_equal(inverse_delta_transform(delta, y_prev), expected)
