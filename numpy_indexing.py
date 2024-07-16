#! /usr/bin/env python3
"""
NumPy indexing
"""

import numpy as np


def main():
    rng = np.random.default_rng(seed=0)
    print("One dimensional arrays")
    x1 = rng.integers(low=0, high=10, size=6)
    print("x1")
    print(x1)
    print("from the start, specify [0], [1], etc.")
    print("the first value x1[0]:", x1[0])
    print("from the end, specify [-1], [-2], etc.")
    print("the last value x1[-1]:", x1[-1])
    print("Two dimensional arrays")
    x2 = rng.integers(low=0, high=10, size=(3, 4))
    print("x2")
    print(x2)
    print("The first row, first column value:", x2[0, 0])
    print("The last row, last column value  :", x2[-1, -1])
    print("Three dimensional arrays")
    x3 = rng.integers(low=0, high=10, size=(3, 4, 5))
    print("x3")
    print(x3)
    print("blan", x3[0, 0, 0])
    print("blan", x3[0, -1, -1])
    print("blan", x3[1, 2, 2])


if __name__ == "__main__":
    main()
