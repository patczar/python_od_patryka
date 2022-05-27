from iter_sprzedaz import IteratorTransakcji

miasto = 'Białystok'
# oblicz sumę wartości transakcji w tym mieście
suma = 0

with IteratorTransakcji('sprzedaz.csv') as maszyna_wczytujaca:
    for rekord in maszyna_wczytujaca:
        if rekord.miasto == miasto:
            suma += rekord.wartosc

print(suma)
