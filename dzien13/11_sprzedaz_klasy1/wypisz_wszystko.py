from sprzedaz import wczytaj_plik

lista = wczytaj_plik('sprzedaz.csv')
print('Wczytano listę:', len(lista))

for rekord in lista:
    print(rekord)
