
# Gdy parametr funkcji jest poprzedzony *
# to wywołując funkcję można przekazać dowolnie wiele argumentów,
# a do funckji trafia
def srednia(*liczby):
    # print(type(liczby)) # to jest tuple / krotka
    suma = 0
    ilosc = 0
    for liczba in liczby:
        suma += liczba
        ilosc += 1
    return suma / ilosc


x = 3
y = 4

print(srednia(x, y))
print(srednia(10, 20, 30, 40, 50, 60))
print(srednia(x))

prawdziwa_lista = [2, 4, 54, 2, 4, 5, 645]
print(srednia(*prawdziwa_lista))
print()

def abc(x, y, z):
    print(f'x = {x} , y = {y}, z = {z}')


abc(5, 10, 15)

lista = ['Ala', 'Ola', 'Ela']
abc(*lista)

abc(lista[0], lista[1], lista[2])

