from typing import List
from decimal import Decimal

from collections import namedtuple

# Transakcja = namedtuple('Transakcja', 'data,miasto,sklep,kategoria,towar,cena,sztuk')
Transakcja = namedtuple('Transakcja', ['data', 'miasto', 'sklep', 'kategoria', 'towar', 'cena', 'sztuk'])

def wczytaj_plik(sciezka:str) -> List['Transakcja']:
    lista = []
    with open(sciezka, mode='r', encoding='UTF-8') as plik:
        plik.readline()
        for linia in plik:
            t = linia.strip().split(',')
            lista.append(Transakcja(*t[0:5], Decimal(t[5]), int(t[6])))
    return lista
