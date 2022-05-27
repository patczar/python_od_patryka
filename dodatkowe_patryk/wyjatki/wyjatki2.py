# W tym programie nie wyłapujemy wyjątków.
# Jeśli zdarzy się wyjątek (zły format liczby, dzielenie przez zero, albo przerwanie programu Ctrl+C),
# to program kończy się natychmiast, a na "standardowe wyjście błędów" wypisuje się opis wyjątku, w tym tzw. stack trace (w Pythonie "traceback")

# Tutaj więcej funkcji, aby zobaczyć czym jest Traceback

def procedura1():
    procedura2()

def procedura2():
    procedura3()

def procedura3():
    x = int(input('Podaj pierwszą liczbę: '))
    y = int(input('Podaj drugą liczbę: '))
    iloraz = podziel(x, y)
    print('Wynik dzielenia:', iloraz)
    sprawdz(iloraz)
    print('OK')

def podziel(x,y):
    return x / y


def sprawdz(liczba):
    if liczba == 13:
        raise ValueError('pechowa trzynastka')


print('Dzień dobry')
procedura1()
print('Koniec programu')
