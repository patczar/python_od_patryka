# W tej wersji oprócz klasy Osoba stworzymy jeszcze klasę Konto

# W prawdziwych projektach klasy definiuje się  zwykle w oddzielnych plikach i importuje do pozostałych plików.
# Tutaj umieszczam wiele klas w jednym pliku, aby wygodnie tworzyć kolejne wersje.

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


class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, saldo = {self._saldo}, wł. {self._wlasciciel}'

    # przykład metod, które modyfikują stan obiektu
    # generalnie klasy, których obiekty mogą się zmieniać w czasie życia, to klasy "mutowalne" (mutable)
    # a klasy, których obiekty się nie zmieniają, np. str, to klasy "niemutowalne" (immutable)
    def wplata(self, kwota):
        self._saldo += kwota

    def wyplata(self, kwota):
        self._saldo -= kwota


ala = Osoba('Ala', 'Kowalska', 30)
konto = Konto(1, ala, 5000)
print(konto)
konto.wplata(333)
print(konto)
konto.wyplata(133)
print(konto)
