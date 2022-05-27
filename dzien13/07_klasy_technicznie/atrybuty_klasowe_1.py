# My uczyliśmy się tworzenia atrybutów w metodzie init
# Ale w Pythonie można też definiować atrybuty na poziomie klasy, jka np. w C++ czy Javie.

# Ale to działa dziwnie...

class Osoba:
    imie = 'imie'
    nazwisko = 'nazwisko'

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Student(Osoba):
    # ta lista będzie współdzielona przez wszystkie obiekty
    # analogia: zmienne statyczne w Javie czy C#
    oceny = []

    def dodaj_ocene(self, ocena):
        # dwie pierwsze wersje dają efekt "wspólnej listy dla wszystkich studentów"
        self.oceny.append(ocena)
        # self.oceny += [ocena]
        # trzecia wersja działa poprawnie, ale to mało wydajne...
        # self.oceny = self.oceny + [ocena]

    def srednia(self):
        return sum(self.oceny) / len(self.oceny)

    def __str__(self):
        return super().__str__() + f' z ocenami {self.oceny}'


o = Osoba()
print(o.imie)
print(o)
o.imie = 'Jan'
o.nazwisko = 'Kowalski'
print(o)
print()


a = Student()
print(a)
a.imie = 'Adam'
a.nazwisko = 'Abacki'
print(a)
print()

b = Student()
print(b)
b.imie = 'Bartek'
b.nazwisko = 'Babecki'
print(b)

print()
print(a)
print(b)
# Do tej pory to działało dobrze

a.dodaj_ocene(5)
a.dodaj_ocene(5)
a.oceny.append(5)
print(a, a.srednia())

print()
b.dodaj_ocene(3)

print(a, a.srednia())

print('Oceny Adama:', a.oceny)
print('Oceny Bartka:', b.oceny)

# Morał: to jest TA SAMA lista
# Atrybut oceny jest tworzony w klasie!!!
# Różne obiekty mają do niego dostęp, ale to jest ten sam obiekt

# Ze stringami nie ma problemu, bo stringi sa "niemutowalne" i w obiektach możemy wpisac inne stringi - ale to będą nowe obiekty
# Ale lista jest "mutowalna" i obiekty mogą modyfikować wspólny obiekt - wspólną listą.
