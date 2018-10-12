def verify(isbn):
    filtered = [
        int(c) if c != "X" else 10 for c in isbn if c.isdigit() or c == "X"
    ]

    if len(filtered) != 10 or 10 in filtered[:-1]:
        return False

    return sum(a*b for a, b in zip(range(10, 0, -1), filtered)) % 11 == 0
