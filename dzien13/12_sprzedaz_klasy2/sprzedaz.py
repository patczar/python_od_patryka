from typing import List
from decimal import Decimal

class Transakcja:
    def __init__(self, data:str, miasto:str, sklep:str, kategoria:str, towar:str, cena:str, sztuk:str):
        self.data = data
        self.miasto = miasto
        self.sklep = sklep
        self.kategoria = kategoria
        self.towar = towar
        self.cena = Decimal(cena)
        self.sztuk = int(sztuk)

    def __str__(self) -> str:
        return f'Transakcja z dnia {self.data} w mieście {self.miasto}: {self.sztuk} towaru {self.towar} w cenie {self.cena}'

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
                lista.append(Transakcja(*t))
        return lista
