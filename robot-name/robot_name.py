import string
import random


class Robot(object):

    names_used = set()

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self._random_name()

    @classmethod
    def _random_name(cls) -> str:
        def gen_name() -> str:
            letters = [random.choice(string.ascii_uppercase) for _ in range(2)]
            numbers = [random.choice(string.digits) for _ in range(3)]

            return "".join(letters+numbers)

        name = gen_name()

        while name in cls.names_used:
            name = gen_name()

        cls.names_used.add(name)

        return name
