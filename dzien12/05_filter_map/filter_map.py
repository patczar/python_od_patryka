from random import randint

liczby = [randint(1, 100) for i in range(20)]
print(liczby)

# Aby wypisać tylko liczby spełniające warunek, np. tylko podzielne przez 2,
# można:

for liczba in liczby:
    if liczba % 2 == 0:
        print(liczba, end=' ')
print()
print('#' * 40)

# Można też uzyskać listę parzystych za pomocą list comprehension ("wyrażenie listotwórcze")
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)

# Istnieje też funkcja filter, która zwraca zetaw tych elementów listy (lub innej kolekcji),
# które spełniają podany warunek.
# Warunek podaje się w formie funkcji, która dostaje wartość i zwraca True/False.
# Na takie funkcje mówi się "predykat".
parzyste2 = filter(lambda x: x%2 == 0, liczby)
print(parzyste2)
for p in parzyste2:
    print(p, end=', ')
print()

# Wyjaśnie dlaczego dodatkowa pętla:
# filter zwraca w wyniku "generator", czyli obiekt, który zwraca wartości dopiero, gdy jest o to proszony, np. w pętli for

# Można też od razu zrzutować to na listę
print(list(filter(lambda x: x%2 == 0, liczby)))
print()

# Z kolei gdy chcemy zastosować jakąśfunkcję ,np. podnoszenie do kwadratu, dla każdego elementu listy,
# to możemy:
# napisać klasyczną pętlę

for liczba in liczby:
    print(liczba**2, end=', ')
print()

# możemy użyć list comprehension
kwadraty = [x**2 for x in liczby]
print(kwadraty)

# albo użyć map
kwadraty2 = map(lambda x: x**2, liczby)
print(kwadraty2)
for k in kwadraty2:
    print(k, end=', ')
print()

print(list(map(lambda x: x**2, liczby)))

# połączenie obu technik
for liczba in liczby:
    if liczba % 2 == 0:
        print(liczba**2, end=' ')
print()

parzyste_kwadraty = [x**2 for x in liczby if x % 2 ==0]
print(parzyste_kwadraty)

pk2 = list(map(lambda x: x**2, filter(lambda x: x % 2 ==0, liczby)))
print(pk2)

# To staje się łądniejsze w zapisie, gdy mamy funkcję, której chcemy użyć
def jest_parzysta(liczba):
    return liczba % 2 == 0

def kwadrat(x):
    return x**2

pk3 = list(map(kwadrat, filter(jest_parzysta, liczby)))
print(pk3)

print()

miasta = ['Warszawa', 'Kraków', 'Gdańsk']

for m in map(str.upper, miasta):
    print(m)
print()

print('Poznań'.upper())
print(str.upper('Łódź')) # Łódź jest parametrem self

dodaj = int.__add__
print(dodaj(13, 43))
