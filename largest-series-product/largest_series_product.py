from operator import mul
from functools import reduce


def largest_product(series, size):
    if size == 0:
        return 1
    if not (0 < size <= len(series)):
        raise ValueError("Invalid size")

    digits = list(map(int, (d for d in series)))
    windows = (digits[i:i+size] for i in range(len(series)-size+1))

    return max(reduce(mul, w) for w in windows)
