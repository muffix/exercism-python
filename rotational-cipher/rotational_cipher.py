def rotate(text, key):
    return "".join([shift(c, key) for c in text])


def shift(char, offset):
    def shift_with_start(char, start, offset):
        return chr((ord(char) - ord(start) + offset) % 26 + ord(start))

    if "a" <= char <= "z":
        return shift_with_start(char, "a", offset)

    if "A" <= char <= "Z":
        return shift_with_start(char, "A", offset)

    return char
