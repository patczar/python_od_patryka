from gen_sprzedaz import Transakcja

miasto = 'Radom'
suma = 0

for rekord in Transakcja.wczytaj_plik_gen('sprzedaz.csv'):
    if rekord.miasto == miasto:
        suma += rekord.wartosc

print(suma)
