x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op == '+':
    wynik = x + y
elif op == '-':
    wynik = x - y
elif op == '*':
    wynik = x * y
elif op == '^':
    wynik = x ** y
elif op == '/':
    if y == 0:
        wynik = 'Dzielenie przez zero!'
    else:
        wynik = x / y
else:
    wynik = 'Nieznana operacja'

print('Wynik:', wynik)
