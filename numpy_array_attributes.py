#! /usr/bin/env python3
"""
NumPy array attributes
"""

import numpy as np


def main():
    rng = np.random.default_rng(seed=13)
    x1 = rng.integers(low=0, high=10, size=6)
    print("x1")
    print(x1)
    print("x1 ndim :", x1.ndim)
    print("x1 shape:", x1.shape, "6 elements in a single row")
    print("x1 size :", x1.size)
    print("x1 dtype:", x1.dtype)
    print("reshape x1 as 6 rows and 1 column")
    x1_reshaped = x1.reshape(6, 1)
    print(x1)
    print("x1_reshaped ndim :", x1_reshaped.ndim)
    print("x1_reshaped shape:", x1_reshaped.shape)
    print("x1_reshaped size :", x1_reshaped.size)
    print("x1_reshaped dtype:", x1_reshaped.dtype)
    x2 = rng.integers(low=0, high=10, size=(3, 4))
    print("x2")
    print(x2)
    print("x2 ndim :", x2.ndim)
    print("x2 shape:", x2.shape)
    print("x2 size :", x2.size)
    print("x2 dtype:", x2.dtype)
    x3 = rng.integers(low=0, high=10, size=(3, 4, 5))
    print("x3")
    print(x3)
    print("x3 ndim :", x3.ndim)
    print("x3 shape:", x3.shape)
    print("x3 size :", x3.size)
    print("x3 dtype:", x3.dtype)

if __name__ == "__main__":
    main()
