def is_pangram(sentence):
    return len(set(c for c in sentence.lower() if 'a' <= c <= 'z')) == 26
