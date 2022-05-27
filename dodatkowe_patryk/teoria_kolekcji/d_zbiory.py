# Zbiór (set)
zbior = {'Katowice', 'Gliwice', 'Ruda Śląska', 'Katowice', 'Chorzów', 'Bytom'}
print(zbior, 'liczba elementów:', len(zbior))

# Specyfika zbiorów:
# zbiory NIE zawierają duplikatów (dodanie duplikatu nie powoduje błędu, ale po prostu nie jest już uwzględniane)
# kolejność NIE jest zachowywana
# NIE można indeksować (zbior[i] nie działa, inaczej mówiąc zbiór NIE JEST sekwencją)
# print(zbior[2])
# zbiory są "mutowalne" (mutable)

# dodawanie i usuwanie elementów:
zbior.add('Sosnowiec')
print(zbior)

zbior.add('Sosnowiec')
print(zbior)

zbior.remove('Sosnowiec')
print(zbior)

# Usunięcie elementu, którego nie ma
# zbior.remove('Sosnowiec') # KeyError: 'Sosnowiec'

# Tak można sprawdzić czy kolekcja zawiera element:
if 'Zabrze' in zbior:
	print('TAK')
else:
	print('NIE')

# Takie sprawdzenie dla zbiorów jest wydajne (dzięki haszkodom itp. rozwiązaniom),
# a dla list i tupli jest niewydajne (Python w pętli przegląda całą zawartość)

# Typowe zastosowania zbiorów:
# - gdy zależy nam na braku duplikacji
# - gdy potrzebujemy móc szybko sprawdzić czy jakiś element istnieje, czy nie istnieje

# Pusty zbiór: tylko w ten sposób
pusty_zbior = set()
print(type(pusty_zbior), pusty_zbior)
print()

# Bo {} jest pustym słownikiem

# Dla zbiorów są dostępne operatory zbiorów, tzw. operacje teoriomnogościowe
# tylko dla zbiorów (a nie dla np. list)

z1 = {'Ala', 'Ola', 'Ela'}
z2 = {'Ola', 'Kasia'}

print('Pierwszy: ', z1)
print('Drugi: ', z2)


print('Suma zbiorów: ', z1 | z2)
print('Iloczyn zbiorów: ', z1 & z2) # inaczej: przecięcie, część wspólna
print('Różnica zbiorów: ', z1 - z2)
print('Różnica zbiorów: ', z2 - z1)
print('Różnica symetryczna: ', z1 ^ z2) # elementy, które są jednym lub drugim, ale nie w obu na raz
print()

# Kolekcje jednych typów można łatwo konwertować na inny typ:

lista = [20, 10, 20, 30, 10, 20, 100]
zbior = set(lista)
print('lista:', lista)
print('zbior:', zbior)

lista = list(zbior)
print('lista:', lista)

napis = 'ala ma kota'
literki = set(napis)
print('literki bez powtórzeń:', literki)
