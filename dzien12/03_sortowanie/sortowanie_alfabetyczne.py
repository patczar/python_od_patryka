lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Żyrardów', 'Zielona Góra', 'Wąchock', 'Wadowice']

print(lista)
print(sorted(lista))

### Sortowanie tekstów zgodnie z alfabetem polskim (i nie tylko) ###

import locale
# Zauważmy, że w tym miejscu jeszcze nie ma poprawnego sortowania
print(locale.getlocale(locale.LC_COLLATE))
print('Łukasz' < 'Marcin')
print(locale.strcoll('Łukasz', 'Marcin') < 0)
print(sorted(lista, key=locale.strxfrm))
print()

# Trzeba ustawić język w module locale
# Można ustawić na konkretny
locale.setlocale(locale.LC_COLLATE, 'Polish') # albo LC_ALL
print(locale.getlocale(locale.LC_COLLATE))
print('Łukasz' < 'Marcin')
print(locale.strcoll('Łukasz', 'Marcin') < 0)
# strcoll daje w wyniku 0, jeśli oba teksty są równe,
# wartość ujemną, jeśli pierwszy jest mniejszy od drugiego
# wartość dodatnią, jeśli pierwszy jest większy od drugiego
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_COLLATE, 'pl_PL')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_COLLATE, 'French')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_COLLATE, 'fr_FR.UTF8')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()


# Gdy podamy pusty string, to przyjmowane są bieżące ustawienia z systemu
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

# Jak działa sama funkcja strxfrm?
# Na podstawie tekstu źródłowego zwraca "techniczny" tekst, który sortowany już po kodach unicode/ascii da właściwą kolejność
print(locale.strxfrm('zebra'))
print(repr(locale.strxfrm('zebra')))
print(repr(locale.strxfrm('żebra')))
print(repr(locale.strxfrm('żółw')))
