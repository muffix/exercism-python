from collections import Counter


def is_isogram(string: str):
    counter = Counter(c for c in string.lower() if 'a' <= c <= 'z')

    return sum(counter.values()) == len(counter)
