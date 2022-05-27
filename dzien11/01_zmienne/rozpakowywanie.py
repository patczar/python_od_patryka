# Gdy mam krotkę
krotka = ('Ala', 5, 'kotów')
# a nawet inną sekwencję, np. listę
lista = ['Ola', 5, 'psów']


osoba, ile, zwierze = krotka
print(f'{osoba} ma {ile} {zwierze}')

osoba, ile, zwierze = lista
print(f'{osoba} ma {ile} {zwierze}')

# Gdy wpisujemy wartość do tupli, to nie zwykle trzeba brać tego w nawiasy
krotka = 'Ala', 5, 'kotów'
print(type(krotka))
osoba, ile, zwierze = krotka
print(f'{osoba} ma {ile} {zwierze}')
print()
# Stąd możliwe takie zapisy:

x, y, z = 10, 20, 30
print('x =', x, '   y =', y)
x, y = y, x
print('x =', x, '   y =', y)
print()

def dzielenie_z_reszta(x, y):
    return x // y, x % y

iloraz, reszta = dzielenie_z_reszta(10, 3)
print(f'10 podzielić na 3 daje wynik {iloraz} i {reszta} reszty.')

tupla = dzielenie_z_reszta(10, 3)
print(f'10 podzielić na 3 daje wynik {tupla[0]} i {tupla[1]} reszty.')

iloraz, reszta = dzielenie_z_reszta(28, 5)
print(f'10 podzielić na 3 daje wynik {iloraz} i {reszta} reszty.')
print()

slownik = {
    'Warszawa': 2_000_000,
    'Kraków': 800_000,
    'Łódź': 750_000,
}

for miasto, populacja in slownik.items():
    print(f'{miasto} ma {populacja} mieszkańców')

# Technicznie można też tak, ale jest brzydko
for entry in slownik.items():
    print(f'{entry[0]} ma {entry[1]} mieszkańców')

