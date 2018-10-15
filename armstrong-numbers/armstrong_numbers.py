def is_armstrong(n):
    num_digits = count_digits(n)
    acc, target = 0, n

    while n:
        acc += int(n % 10)**num_digits
        n /= 10

    return acc == target


def count_digits(n: int) -> int:
    i = 1

    if n > 1e8:
        i += 8
        n /= 1e8
    if n > 1e4:
        i += 4
        n /= 1e4
    if n > 1e2:
        i += 2
        n /= 1e2
    if n > 10:
        i += 1

    return i
