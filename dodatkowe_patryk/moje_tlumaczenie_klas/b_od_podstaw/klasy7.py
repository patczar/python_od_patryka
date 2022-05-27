class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Jestem Osobą. Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

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

    # Co podklasa może zrobić z metodami?
    # 1. Może nie robić nic. Np. w nadklasie mamy metodę peloletnia() , której w podklasie w żaden sposób nie zmieniamy.
    #    Efekt jest taki, że na obiekcie klasy Student można wywołać tę metodę i działa tak jak zdefiniowano w klasie Osoba.

    # 2. W podklasie możemy dodać nowe metody, których nie było w nadklasie.
    #   Efekt: tylko na obiektach Student można wywoływać metody dot. ocen. Nie ma tych metod w obiektach Osoba.
    def dodaj_ocene(self, ocena):
        return self.oceny.append(ocena)

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)

    # 3. W podklasie można nadpisać metodę, która była zdefiniowana w nadklasie.  "overriding"
    #    Efekt: zarówno na obiektach nadklasy (Osoba), jak i na obiektach podklasy (Student)
    #    można wywoływać taką samą metodę, ale zadziała ona w inny sposób dla zwykłych osób, a w inny dla studentów.
    #    Na to mówi się "polimorfizm".
    def przedstaw_sie(self):
        print(f'Jestem Studentem. Nazywam się {self.imie} {self.nazwisko} i studiuję na {self.rok} roku kierunku {self.kierunek}.')

    def __str__(self):
        return super().__str__() + f', student {self.rok} roku kierunku {self.kierunek}'

    def __repr__(self):
        return f'Student({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)}, {repr(self.rok)}, {repr(self.kierunek)})'


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f'Jestem Pracownikiem. Nazywam się {self.imie} {self.nazwisko} i pracuję jako {self.stanowisko}, zarabiam {self.pensja}.')

    def __str__(self):
        return super().__str__() + f', {self.stanowisko}, zarobki: {self.pensja}'


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

def main():
    osoba = Osoba('Ala', 'Kowalska', 40)
    student = Student('Jan', 'Kowalski', 23, 4, 'geografia')

    print('osoba:', osoba)
    print('student:', student)

    # student posiada te atrybuty i metody, które odziedziczył z klasy Osoba
    print(osoba.imie)
    print(student.imie)

    osoba.przedstaw_sie()
    student.przedstaw_sie()
    print(student.pelnoletnia())

    # Ale tylko Student posiada nowe atrybuty i metody, które zostały dopisane w klasie Student
    # print(osoba.rok, 'rok studiów na kierunku', osoba.kierunek)
    print(student.rok, 'rok studiów na kierunku', student.kierunek)

    #ERR osoba.dodaj_ocene(3.0)
    student.dodaj_ocene(5)
    student.dodaj_ocene(4)
    print(student.srednia_ocen())


if __name__ == '__main__':
    main()
