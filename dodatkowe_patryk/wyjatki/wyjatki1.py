# W tym programie nie wyłapujemy wyjątków.
# Jeśli zdarzy się wyjątek (zły format liczby, dzielenie przez zero, albo przerwanie programu Ctrl+C),
# to program kończy się natychmiast, a na "standardowe wyjście błędów" wypisuje się opis wyjątku, w tym tzw. stack trace (w Pythonie "traceback")

print('Dzień dobry')
x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
iloraz = x / y
print('Wynik dzielenia:', iloraz)
print('Koniec programu')
