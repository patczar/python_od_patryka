def gcd(a: int, b: int) -> int:
    '''Największy wspólny dzielnik, algorytm Euklidesa - zapis "pajtoniczny".
       Istnieje też gotowa funkcja math.gcd
    '''
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, nominator: int = 0, denominator: int = 1):
        if denominator == 0:
            raise ValueError('Fraction denominator cannot be zero')
        if denominator < 0:
            nominator = -nominator
            denominator = -denominator
        self.nominator = nominator
        self.denominator = denominator

    def __repr__(self) -> str:
        return f'Fraction({repr(self.nominator)},{repr(self.denominator)})'

    def __str__(self) -> str:
        return f'[{self.nominator}/{self.denominator}]'

    def shortened(self) -> 'Fraction':
        gcd_here = gcd(self.nominator, self.denominator)
        return Fraction(self.nominator // gcd_here, self.denominator // gcd_here)

    def reciprocal(self) -> 'Fraction':
        return Fraction(self.denominator, self.nominator)

    @property
    def integer_part(self) -> int:
        return self.nominator // self.denominator

    @property
    def fraction_part(self) -> 'Fraction':
        return Fraction(self.nominator % self.denominator, self.denominator)

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.nominator, self.denominator)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        # wersja praktyczna: najpierw mnożę mianowniki, później skracam wynik
        return Fraction(self.nominator * other.denominator + other.nominator * self.denominator,
                        self.denominator * other.denominator).shortened()

    def __add__v1_(self, other: 'Fraction') -> 'Fraction':
        # wersja "szkolna" ze sprowadzaniem do wspólnego mianownika
        common_denom = self.denominator * other.denominator // gcd(self.denominator, other.denominator)
        nom1 = self.nominator * common_denom // self.denominator
        nom2 = other.nominator * common_denom // other.denominator
        return Fraction(nom1 + nom2, common_denom)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        return self + (-other)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.nominator * other.nominator,
                        self.denominator * other.denominator).shortened()

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        return self * other.reciprocal()

    def __floordiv__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(int(self / other))

    def __mod__(self, other: 'Fraction') -> 'Fraction':
        # Moja interpretacja co może znaczyć "reszta z dzielenia" dla ułamków. Zrealizowane za pomocą innych operacji.
        return self - self // other

    # Rzutowania na inne typy: float, int, bool
    def __float__(self) -> float:
        return self.nominator / self.denominator

    def __int__(self) -> int:
        return self.integer_part

    def __bool__(self) -> bool:
        return self.nominator != 0

    # Porównania. ne, gt i ge będą działać z automatu
    def __eq__(self, other: 'Fraction') -> bool:
        return self.nominator * other.denominator == other.nominator * self.denominator

    def __lt__(self, other: 'Fraction') -> bool:
        return self.nominator * other.denominator <  other.nominator * self.denominator

    def __le__(self, other: 'Fraction') -> bool:
        return self.nominator * other.denominator <= other.nominator * self.denominator
