from sprzedaz import wczytaj_plik

lista = wczytaj_plik('sprzedaz.csv')
print('Wczytano listę:', len(lista))

for rekord in lista:
    print(rekord)

print()

print(lista[333])
print(lista[333][0])
print(lista[333].data)
print(lista[333].data[:4])
