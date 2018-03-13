class Rational_1(object):
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n%m, m
        return n

    def __init__(self, num, den=1):
        if (not isinstance(num, (int, float)) or 
            not isinstance(den, (int, float)) ):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        # call function _gcd defined in this class
        if isinstance(num, int) and isinstance(den, int):
            g = Rational._gcd(num, den)
            self._num = sign * (num // g)
            self._den = (den // g)
        if isinstance(num, float) or isinstance(den, float):
            num_tuple = float(num).as_integer_ratio()
            den_tuple = float(den).as_integer_ratio()
            g = Rational._gcd(num_tuple[0] * den_tuple[1],
                              num_tuple[1] * den_tuple[0])
            self._num = sign * num_tuple[0] * den_tuple[1] // g
            self._den = num_tuple[1] * den_tuple[0] // g

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, another):
        den = self._den * another.den()
        num = (self._den * another.num() +
               self._num * another.den())
        return Rational(num, den)

    def __sub__(self, another):
        den = self._den * another.den()
        num = (self._den * another.num() -
               self._num * another.den())
        return Rational(num, den)

    def __mul__(self, another):
        den = self._den * another.den()
        num = self._num * another.num()
        return Rational(num, den)

    def __floordiv__(self, another):
        den = self._den * another.num()
        num = self._num * another.den()
        return Rational(num, den)

    def __eq__(self, another):
        return self._num * another.den() == self._den * another.num()

    def to_int(self):
        return self._num // self._den

    def to_float(self):
        return self._num / self._den

    def print(self):
        print('{}/{}'.format(self._num, self._den))

Rational_1(2.5, 3).print()
