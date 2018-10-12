import re

from collections import defaultdict


def word_count(phrase):
    counts = defaultdict(int)
    words = (w for w in re.split("[^a-zA-Z0-9']", phrase.lower()) if w)

    for word in words:
        if word[0] == word[-1] == "'":
            word = word[1:-1]
        counts[word] += 1

    return counts
