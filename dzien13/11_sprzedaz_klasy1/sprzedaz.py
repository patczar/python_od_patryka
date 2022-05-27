class Transakcja:
    def __init__(self, data:str, miasto:str, sklep:str, kategoria:str, towar:str, cena:float, sztuk:int):
        self.data = data
        self.miasto = miasto
        self.sklep = sklep
        self.kategoria = kategoria
        self.towar = towar
        self.cena = cena
        self.sztuk = sztuk

    def __str__(self) -> str:
        return f'Transakcja z dnia {self.data} w mieście {self.miasto}: {self.sztuk} towaru {self.towar} w cenie {self.cena}'

    @property
    def wartosc(self) -> float:
        return self.cena * self.sztuk


from typing import List

def wczytaj_plik(sciezka:str) -> List[Transakcja]:
    """
    Funkcja czyta dane z pliku.

    :param sciezka: ścieżka do pliku CSV
    :return: lista obiektów Transakcja wczytanych z pliku
    """
    lista = []
    with open(sciezka, mode='r', encoding='UTF-8') as plik:
        plik.readline() # pominięcie pierwszej linii - nagłówki
        for linia in plik:
            t = linia.strip().split(',')
            transakcja = Transakcja(t[0], t[1], t[2], t[3], t[4], float(t[5]), int(t[6]))
            lista.append(transakcja)
    return lista
