from math import sqrt


def primitive_triplets(number_in_triplet):
    if number_in_triplet % 4 != 0:
        raise ValueError("Number must be divisible by 4")

    return {
        tuple(sorted((m**2 - n**2, number_in_triplet, m**2 + n**2)))
        for (m, n) in factors(number_in_triplet/2)
        if gcd(m, n) == 1
    }


def triplets_in_range(range_start, range_end):
    triplets = set()

    for i in range(range_start, range_end):
        for j in range(i, range_end):
            candidate = (i, j, int(sqrt(i*i+j*j)))
            if candidate[2] <= range_end and is_triplet(candidate):
                triplets.add(candidate)

    return triplets


def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def factors(n):
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            yield (n/i, i)
