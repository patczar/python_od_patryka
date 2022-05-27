from typing import List
from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Transakcja:
    data: str
    miasto: str
    sklep: str
    kategoria: str
    towar: str
    cena: Decimal
    sztuk: int

    @property
    def wartosc(self) -> Decimal:
        return self.cena * self.sztuk


# W tej wersji zamiast czytać cały plik od razu do postaci listy obiektów,
# utworzymy iterator, który będzie zwracał kolejne rekordy.
# Dałoby nam to możliwość czytania bardzo dużych plików, które nie mieszczą się w pamięci, a jednocześnie pracę z obiektami.

class IteratorTransakcji:
    def __init__(self, sciezka):
        self.sciezka = sciezka

    def __enter__(self):
        self.plik = open(self.sciezka, mode='r', encoding='UTF-8')
        self.plik.readline() # pomijamy nagłówek CSV
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.plik.close()

    def __iter__(self):
        return self

    def __next__(self) -> Transakcja:
        linia = self.plik.readline()
        if not linia:
            raise StopIteration
        t = linia.strip().split(',')
        return Transakcja(*t[0:5], Decimal(t[5]), int(t[6]))


# Dzięki umieszczniu treści programu w funkcji main,
# wszystkie zmienne są zmiennymi lokalnymi, nie tworzę zmiennych globalnych
def main():
    with IteratorTransakcji('sprzedaz.csv') as it:
        for transakcja in it:
            print(transakcja)

# Dzięki takiemu if-owi, treść programu wykona się tylko wtedy,
# gdy ten plik jest uruchamiany bezpośrednio jako program,
# a nie wykona się, gdy ten plik jest importowany przez inny.
if __name__ == '__main__':
    main()
