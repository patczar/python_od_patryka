# Uwaga, wyłapywanie WSZYSTKICH wyjątków jest ryzykowne,
# bo wówczas nie da się przerwać programu za pomocą Ctrl+C (jeśli tak jak poniższy działa w pętli)

print('Dzień dobry')

while True:
    try:
        x = int(input('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        iloraz = x / y
        print('Wynik dzielenia:', iloraz)
    except:
        print('Wystąpił jakiś błąd')
    print('ciąg dalszy...')


print('Koniec programu')
