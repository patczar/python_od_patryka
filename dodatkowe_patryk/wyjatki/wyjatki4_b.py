print('Dzień dobry')

try:
    while True:
        try:
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            iloraz = x / y
            print('Wynik dzielenia:', iloraz)
            if iloraz == 13:
                raise ValueError('pechowa trzynastka')
            print('Generalnie jest OK')
        # ten except nie wyłapie wyjątku KeyboardInterrupt, więc nciśnięcie Ctrl+C skutecznie przerwie program
        except Exception as e:
            print(f'Wystąpił błąd typu {type(e)} : {e}')
except KeyboardInterrupt:
    print('\nKończymy? OK...')

print('Koniec programu')
