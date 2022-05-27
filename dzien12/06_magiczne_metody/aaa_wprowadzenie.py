# Gdy tworzymy klasę, to możemy w tej klasie zdefiniować nie tylko nowe, wymyślone przed siebie metody,
# ale możemy także zdefiniować ("nadpisać") jedną ze specjalnych metod Pythona, które decydują o zachowaniu
# obiektu w określonych sytuacjach.

# Np. definiując __str__ określamy jaki napis pojawi się, gdy obiekt naszej będzie wypisywany.

# Niektóre z tych metod, np. __add__, pozawalją nam określoć działanie operatorów )(np. +) dla wartości tego typu
class Liczba:
    def __init__(self, wartosc=0):
        self.wartosc = wartosc

    def __str__(self):
        return f'[{self.wartosc}]'

    def __add__(self, other):
        return Liczba(self.wartosc + other.wartosc)

    def __sub__(self, other):
        return Liczba(self.wartosc - other.wartosc)

    def __mul__(self, other):
        return Liczba(self.wartosc * other.wartosc)

    # definiując te 3 operatory porównania, mamy komplet, Python sam uzupełni o ne, gt, ge
    def __eq__(self, other):
        return self.wartosc == other.wartosc

    def __lt__(self, other):
        return self.wartosc < other.wartosc

    def __le__(self, other):
        return self.wartosc <= other.wartosc


x = Liczba(3)
y = Liczba(5)
print(x, y)
z = x + y
print(x, y, z)
print(type(z))

print(x + y + z)

z = y - x
print(z)
print()

print(x, y)
print(x < y)
print(x > y)
print(x == y)
print(x != y)
print(x <= y)
print(x >= y)











a = Liczba('12')
b = Liczba('34')
print(a + b)

