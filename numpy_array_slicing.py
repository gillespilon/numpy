#! /usr/bin/env python3
"""
NumPy slicing
"""

import numpy as np


def main():
    rng = np.random.default_rng(seed=0)
    print("One dimensional arrays")
    x1 = rng.integers(low=0, high=10, size=10)
    print("x1")
    print(x1)
    print("slice the first five elements             :", x1[:5])
    print("slice the first five elements             :", x1[0:5:1])
    print("all elements after the first five elements:", x1[5:])
    print("all elements after the first five elements:", x1[5::1])
    print("every other element                       :", x1[::2])
    print("every other elements starting at index 1  :", x1[1::2])
    print("reverse all elements of the array         :", x1[::-1])
    print("Two dimensional arrays")
    x2 = rng.integers(low=0, high=10, size=(3, 4))
    print("x2")
    print(x2)
    print("rows 0 to 1, columns 0 to 2:              :", x2[:2, :3] )
    print("all rows, every other column:             :", x2[:, ::2])


if __name__ == "__main__":
    main()
