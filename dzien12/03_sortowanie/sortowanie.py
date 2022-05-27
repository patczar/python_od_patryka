lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Żyrardów', 'Zielona Góra', 'Wąchock', 'Wadowice']

print(lista)
print(sorted(lista))
print(lista)
print()

# Do funkcji sorted jako dodatkowy parametry key można podać funkcję,
# która zostanie uruchomiona dla każdego elementu listy i zwróci jego "wagę".
# A elementy listy zostaną posortowane wg uzyskanych "wag", domyślnie rosnąco.

# Przyjmijmy, że dla słowa jako jego wagę zwracamy długość (liczbę liter)
print(sorted(lista, key=lambda s: len(s)))

# Akurat w tym przypadku można bezpośrednio wskazać funkcję len; nie trzeba pisać lambda
print(sorted(lista, key=len))

# Inny przykład: posortujmy wg drugiej litery
print(sorted(lista, key=lambda s: s[1]))

# Tylko, żeby wytłumaczyć kwestię lambdy.
# Taką funkcję biorącą drugi znak z napisu można też zdefiniować tradycyjnie:
def drugi_znak(napis):
   return napis[1]

# i teraz przekazać do sorted
print(sorted(lista, key=drugi_znak))


print()
# Tutaj element 0 uzyska wartość True, a po zrzutowaniu na int to będzie 1
# pozostałe False, a po zrzutowaniu na int to będzie 0.
# Wskazany element (0) będzie na końcu.
xs = [1, 0, 2]
print(sorted(xs, key=lambda x: x==0))



