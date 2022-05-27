from typing import List
from decimal import Decimal
from dataclasses import dataclass

# @dataclass automatycznie generuje metody init, repr, str i eq
# które działają we właściwy sposób dla rekordów z polami takimi, jak wymienione w klasie
# od Pythona 3.7

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
    def wczytaj_plik(sciezka:str) -> List['Transakcja']:
        """
        Funkcja czyta dane z pliku.

        :param sciezka: ścieżka do pliku CSV
        :return: lista obiektów Transakcja wczytanych z pliku
        """
        lista = []
        with open(sciezka, mode='r', encoding='UTF-8') as plik:
            plik.readline()
            for linia in plik:
                t = linia.strip().split(',')
                lista.append(Transakcja(*t[0:5], Decimal(t[5]), int(t[6])))
        return lista
