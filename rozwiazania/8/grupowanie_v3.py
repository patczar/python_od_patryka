from sprzedaz import Transakcja
from collections import defaultdict
from decimal import Decimal

# Różnice względem v1:
# - użycie defaultdict - dzięki temu nie trzeba pisać if-a
# - sorted
def main():
    transakcje = Transakcja.wczytaj_plik('sprzedaz.csv')
    sumy = defaultdict(Decimal)
    for t in transakcje:
        sumy[t.miasto] += t.wartosc

    print(f'{"miasto":^10} → {"suma":^10}')
    for miasto, suma in sorted(sumy.items()):
        print(f'{miasto:10} → {suma:10.2f}')

if __name__ == '__main__':
    main()
