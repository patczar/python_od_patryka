from sprzedaz import Transakcja

# Różnice względem v1:
# - użycie get z wartością domyślną - dzięki temu nie trzeba pisać if-a
# - sorted
def main():
    transakcje = Transakcja.wczytaj_plik('sprzedaz.csv')
    sumy = {}
    for t in transakcje:
        sumy[t.miasto] = sumy.get(t.miasto, 0) + t.wartosc

    print(f'{"miasto":^10} → {"suma":^10}')
    for miasto, suma in sorted(sumy.items()):
        print(f'{miasto:10} → {suma:10.2f}')

if __name__ == '__main__':
    main()
