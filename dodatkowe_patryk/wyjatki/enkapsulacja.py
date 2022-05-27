# Dobrą praktyką w programowaniu obiektowym jest nieodwoływanie się do pól (zmiennych / atrybtów)
# w obiektach poza tą klasą, tylko korzystanie z dedykowanych metod.

# Jeśli będziemy przestrzegać tej zasady, to klasa będzie mogła zapewnić poprawne działanie,
# będziemy mieć pewność, że spełnione są pewne niezmienniki (invariant).

# Np. możemy zapewnić, że saldo nie jest ujemne.
# Dużą rolę w tym pełnią wyjątki.
# Gdy jakaś operacja "widzi", że prowadziłaby do złego stanu, wyrzuca wyjątek.
# Gdy operacja jest przerywana wyjątkiem, to nie powinna ona zmieniać stanu.

class BrakSrodkow(Exception):
    def __init__(self, numer, kwota, saldo):
        super().__init__(f'Brak środków na koncie nr {numer}. Próbowano wypłacić {kwota}, a na koncie jest {saldo}')
        self.numer = numer
        self.kwota = kwota
        self.saldo = saldo


class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        if saldo < 0:
            raise ValueError('ujemne saldo')
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, saldo = {self._saldo}, wł. {self._wlasciciel}'

    def wplata(self, kwota):
        if kwota <= 0:
            raise ValueError('niedodatnia kwota we wplata')
        self._saldo += kwota

    def wyplata(self, kwota):
        if kwota <= 0:
            raise ValueError('niedodatnia kwota w wyplata')
        if kwota > self._saldo:
            raise BrakSrodkow(self._numer, kwota, self._saldo)
        self._saldo -= kwota


konto = Konto(1, 'Ala', 1000)
print(konto)
konto.wplata(200)
print(konto)
konto.wyplata(800)
print(konto)

try:
    konto.wplata(-50)
except Exception as e:
    print(e)

try:
    konto.wyplata(500)
except Exception as e:
    print(e)
