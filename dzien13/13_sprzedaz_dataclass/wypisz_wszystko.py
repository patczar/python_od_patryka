from sprzedaz import Transakcja

lista = Transakcja.wczytaj_plik('sprzedaz.csv')
print('Wczytano listę:', len(lista))

for rekord in lista:
    print(rekord)
