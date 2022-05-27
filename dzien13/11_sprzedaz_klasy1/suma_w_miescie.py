from sprzedaz import wczytaj_plik

miasto = 'Katowice'
# oblicz sumę wartości transakcji w tym mieście
suma = 0

lista = wczytaj_plik('sprzedaz.csv')
print('Wczytano listę:', len(lista))

for rekord in lista:
    if rekord.miasto == miasto:
        suma += rekord.wartosc

print(suma)
print(f'{suma:.2f}')
print('{:.2f}'.format(suma))
print('%.2f' % suma)
