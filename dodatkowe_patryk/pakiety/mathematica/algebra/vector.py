from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def dlugosc(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.dlugosc() < other.dlugosc()

    def __le__(self, other):
        return self.dlugosc() <= other.dlugosc()

    def __gt__(self, other):
        return self.dlugosc() > other.dlugosc()

    def __ge__(self, other):
        return self.dlugosc() >= other.dlugosc()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # to daje możliwość mnożenia wektor * liczba
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    # to daje możliwość mnożenia liczba * wektor
    def __rmul__(self, other):
        return self.__mul__(other)


def main():
    a = Vector(x=10, y=20)
    b = Vector(15, 5)
    zerowy = Vector()
    pionowy = Vector(y=10)
    print(f'a = {a}')
    print(f'b = {b}')
    print()
    suma = a + b
    print(f'suma = {suma}')
    roznica = a - b
    print(f'rozn = {roznica}')
    iloczyn1 = a * 3
    print(f'iloczyn1 = {iloczyn1}')
    iloczyn2 = 5 * b
    print(f'iloczyn2 = {iloczyn2}')
    print()


if __name__ == '__main__':
    main()
