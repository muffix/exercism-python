import math
from itertools import count, takewhile


def sieve(limit):
    if limit < 2:
        return []

    composites = set()
    primes = [2]

    for i in range(3, limit+1, 2):
        if i in composites:
            continue

        primes.append(i)
        composites.update(
            takewhile(lambda x: x < limit, (j*i for j in count(start=2)))
        )

    return primes
