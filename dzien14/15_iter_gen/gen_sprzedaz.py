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


    @staticmethod
    def wczytaj_plik_gen(sciezka):
        with open(sciezka, mode='r', encoding='UTF-8') as plik:
            plik.readline()
            for linia in plik:
                t = linia.strip().split(',')
                yield Transakcja(*t[0:5], Decimal(t[5]), int(t[6]))


def main():
    for transakcja in Transakcja.wczytaj_plik_gen('sprzedaz.csv'):
        print(transakcja)

if __name__ == '__main__':
    main()
