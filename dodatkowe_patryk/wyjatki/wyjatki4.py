print('Dzień dobry')

try:
    x = int(input('Podaj pierwszą liczbę: '))
    y = int(input('Podaj drugą liczbę: '))
    iloraz = x / y
    print('Wynik dzielenia:', iloraz)
    if iloraz == 13:
        raise ValueError('pechowa trzynastka')
    print('Generalnie jest OK')
except Exception as e:
    print(f'Wystąpił błąd typu {type(e)} : {e}')

print('Koniec programu')
