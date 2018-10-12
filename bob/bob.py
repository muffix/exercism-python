def hey(phrase: str):
    phrase = phrase.strip()

    if not phrase:
        return "Fine. Be that way!"

    upper_phrase = phrase.upper()
    is_question = phrase.endswith("?")
    is_allcaps = phrase == upper_phrase and upper_phrase != upper_phrase.lower()

    if is_allcaps and is_question:
        return "Calm down, I know what I'm doing!"
    if is_allcaps:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
