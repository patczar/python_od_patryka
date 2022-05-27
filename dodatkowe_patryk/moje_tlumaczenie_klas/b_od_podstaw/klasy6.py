class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        return self.wiek >= 18

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def __repr__(self):
        return f'Osoba({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)})'


# Klasa Student "dziedziczy z klasy Osoba" albo inaczej mówiąc "jest rozszerzeniem klasy Osoba",
# Student jest podklasą (subclass) klasy Osoba, a Osoba jest nadklasą Studenta (superclass)
# Student, oprócz pól i metod takich jak w klasie Osoba,
# ma zawierać dodatkowe pola rok, kierunek, oceny
# oraz metodę srednia_ocen()
class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, rok, kierunek):
        # dobrą praktyką podczas definiowania __init__ w podklasie jest wywołanie __init__ z nadklasy,
        # aby każdy obiekt podklasy był "co najmiej tak dobry" jak obiekt nadklasy
        super().__init__(imie, nazwisko, wiek)
        self.rok = rok
        self.kierunek = kierunek
        self.oceny = []

    def dodaj_ocene(self, ocena):
        return self.oceny.append(ocena)

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)


class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, saldo = {self._saldo}, wł. {self._wlasciciel}'

    def wplata(self, kwota):
        self._saldo += kwota

    def wyplata(self, kwota):
        self._saldo -= kwota

###############

osoba = Osoba('Ala', 'Kowalska', 40)
student = Student('Jan', 'Kowalski', 23, 4, 'geografia')

print('osoba:', osoba)
print('student:', student)

# student posiada te atrybuty i metody, które odziedziczył z klasy Osoba
print(osoba.imie)
print(student.imie)

osoba.przedstaw_sie()
student.przedstaw_sie()

# Ale tylko Student posiada nowe atrybuty i metody, które zostały dopisane w klasie Student
# print(osoba.rok, 'rok studiów na kierunku', osoba.kierunek)
print(student.rok, 'rok studiów na kierunku', student.kierunek)

student.dodaj_ocene(5)
student.dodaj_ocene(4)
print(student.srednia_ocen())
