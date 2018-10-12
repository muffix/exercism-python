from functools import partial
from collections import Counter


def score(dice, category):
    return category(dice)


def fixed_num(num: int, dice: list) -> int:
    return sum(d for d in dice if d == num)


def yacht(dice: list) -> int:
    return 50 if len(set(dice)) == 1 else 0


def full_house(dice: list) -> int:
    return sum(dice) if sorted(Counter(dice).values(), reverse=True) == [3, 2] else 0


def four_of_a_kind(dice: list) -> int:
    most_common = Counter(dice).most_common(1)[0]
    return 4*most_common[0] if most_common[1] >= 4 else 0


def choice(dice: list) -> int:
    return sum(dice)


def straight(must_contain: int, dice: list) -> int:
    dice = sorted(dice)
    is_straight = all(dice[i] == dice[i+1]-1 for i in range(len(dice)-1))
    return 30 if is_straight and must_contain in dice else 0


    # Score categories
    # Change the values as you see fit
YACHT = yacht
ONES = partial(fixed_num, 1)
TWOS = partial(fixed_num, 2)
THREES = partial(fixed_num, 3)
FOURS = partial(fixed_num, 4)
FIVES = partial(fixed_num, 5)
SIXES = partial(fixed_num, 6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = partial(straight, 1)
BIG_STRAIGHT = partial(straight, 6)
CHOICE = choice
