
dzialania = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

funkcja = dzialania[op]
wynik = funkcja(x, y)
print('Wynik:', wynik)
