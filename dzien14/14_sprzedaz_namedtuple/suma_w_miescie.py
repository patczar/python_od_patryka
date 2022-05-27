from sprzedaz import wczytaj_plik

miasto = 'Katowice'
# oblicz sumę wartości transakcji w tym mieście
suma = 0

lista = wczytaj_plik('sprzedaz.csv')
print('Wczytano listę:', len(lista))

for rekord in lista:
    if rekord.miasto == miasto:
        suma += rekord.cena * rekord.sztuk

print(suma)
