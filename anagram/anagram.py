from collections import Counter


def find_anagrams(word, candidates):
    word = word.lower()
    counts = Counter(word)

    return [c for c in candidates if Counter(c.lower()) == counts and c.lower() != word]
