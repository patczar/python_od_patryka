print('Dzień dobry')

try:
    x = int(input('Podaj pierwszą liczbę: '))
    y = int(input('Podaj drugą liczbę: '))
    iloraz = x / y
    print('Wynik dzielenia:', iloraz)
    if iloraz == 13:
        raise ValueError('pechowa trzynastka')
    print('Generalnie jest OK')

except:
    print('Wystąpił jakiś błąd')
# Tak napisane except wyłapuje wszystkie błędy, tak jakby działało except BaseException

print('Koniec programu')
