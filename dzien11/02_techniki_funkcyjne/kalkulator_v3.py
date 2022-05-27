
dzialania = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y,
}

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op not in dzialania:
    print('Nieznana operacja', op)
else:
    wynik = dzialania[op](x, y)
    print('Wynik:', wynik)
