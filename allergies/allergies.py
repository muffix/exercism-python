from enum import IntFlag


allergens = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]
allergen_scores = {allergen: 1 << i for i, allergen in enumerate(allergens)}


class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.score & allergen_scores[item] > 0

    @property
    def lst(self):
        return [allergen for allergen in allergens if self.is_allergic_to(allergen)]
