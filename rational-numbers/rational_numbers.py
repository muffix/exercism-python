def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


class Rational(object):
    def __init__(self, numer, denom):
        d = gcd(numer, denom)
        self.numer = numer/d
        self.denom = denom/d

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        return self + Rational(-1, 1) * other

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return self * (other ** -1)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power: int):
        if power < 0:
            self.numer, self.denom = self.denom, self.numer
            power = -power

        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base: float):
        return base ** (self.numer / self.denom)
