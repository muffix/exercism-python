def decode(string):
    result = ""
    num = ""

    for c in string:
        if c.isdigit():
            num += c
            continue

        result += c*int(num if num else 1)
        num = ""

    return result


def encode(string):
    def enc_format(char, count):
        if not char:
            return ""

        return f"{count if count > 1 else ''}{char}"

    result = ""

    last = None
    count = 0

    for c in string:
        if c != last:
            result += enc_format(last, count)

            last = c
            count = 1
        else:
            count += 1

    return result + enc_format(last, count)
