from sprzedaz import Transakcja

# Wersja mniej wydajna od następnych. Tutaj najpierw ustalamy zbiór miast, a dopiero później  dla każdego miasta przeglądamy wszystkie transakcje - wiele razy czytamy te same dane...

def main():
    transakcje = Transakcja.wczytaj_plik('sprzedaz.csv')
    print(f'{"miasto":^10} → {"suma":^10}')
    miasta = {t.miasto for t in transakcje}
    for miasto in sorted(miasta):
        suma = 0
        for t in transakcje:
            if t.miasto == miasto:
                suma += t.wartosc
        print(f'{miasto:10} → {suma:10.2f}')

if __name__ == '__main__':
    main()
