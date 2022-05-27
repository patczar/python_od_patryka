# Jeśli odwołamy się do modułu operator, można nie pisaćwyrażeń lambda, tylko bezpośrednio wskazać istniejące funkcje Pythona

import operator

dzialania = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op not in dzialania:
    print('Nieznana operacja', op)
else:
    wynik = dzialania[op](x, y)
    print('Wynik:', wynik)
