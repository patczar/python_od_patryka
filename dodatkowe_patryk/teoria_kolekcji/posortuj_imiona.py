# Program w pętli wczytuje od użytkownika jakieś teksty (przykładowo: imiona)
# i zbiera je do listy. Zbieranie danych kończymy, gdy użytkownik poda pusty napis.
# Wypisz zebrane imiona w jednej linii.
# Znajdź funkcję/metodę służącą do sortowania i posortuj tę listę, wypisz posortowane imiona.

import locale

lista = []
while True:
    imie = input('Podaj kolejne imię: ')
    if not imie: break
    lista.append(imie)

print()
print('Nieposortowane:')
print(lista)
print()

print('Sortuję w sposób domyślny:')
# lista.sort() - sortowanie w miejscu, lista ulega zmianie
# sorted(lista) - zwraca w wyniku nową listę, a nie modyfikuje oryginalnej

lista.sort()
print(lista)
print()

print('Sortuję zgodnie z bieżącym alfabetem:')
locale.setlocale(locale.LC_ALL, '')
lista.sort(key=locale.strxfrm)
print(lista)
print()

print('Sortuję zgodnie z alfabetem French:')
locale.setlocale(locale.LC_ALL, 'French')
lista.sort(key=locale.strxfrm)
print(lista)
print()

print('Sortuję zgodnie z alfabetem Polish:')
locale.setlocale(locale.LC_ALL, 'Polish')
lista.sort(key=locale.strxfrm)
print(lista)
print()

# W starszch wersjach Pythona
# lista.sort(locale.strcoll)
# print(lista)
