# Tworzę własną klasę wyjątku - BrakSrodkow
class BrakSrodkow(Exception):
    pass

class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self, kwota):
        if kwota <= 0:
            raise ValueError('Ujemna kwota w wplata')
        self.saldo += kwota

    def wyplata(self, kwota):
        if kwota <= 0:
            raise ValueError('Ujemna kwota w wyplata')
        if kwota > self.saldo:
            raise BrakSrodkow(f'Brak środków na koncie nr {self.numer}. Żądano {kwota}, a jest {self.saldo}.')
        self.saldo -= kwota
