from sprzedaz import Transakcja

# Klasyczny algorytm grupowania/agregacji z wykorzystaniem słownika.
def main():
    transakcje = Transakcja.wczytaj_plik('sprzedaz.csv')
    sumy = {}
    for t in transakcje:
        if t.miasto in sumy:
            sumy[t.miasto] += t.wartosc
        else:
            sumy[t.miasto] = t.wartosc

    print(f'{"miasto":^10} → {"suma":^10}')
    for miasto, suma in sumy.items():
        print(f'{miasto:10} → {suma:10.2f}')

if __name__ == '__main__':
    main()
