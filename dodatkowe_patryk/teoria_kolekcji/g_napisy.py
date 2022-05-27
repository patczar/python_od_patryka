# Napisy (czyli str) w Pythonie jest sekwencją znaków.
# Można iterować za pomocą pętli for,
# można wycinać fragmenty.
# Stringi są niemutowalne.

napis = 'Ala ma kota'
print(len(napis))

for znak in napis:
	print('Kolejny znak:', znak)
print()

print('Typ napisu:', type(napis))
print('Typ znaku:', type(napis[4]))

print(napis[4])
print(napis[4:6])
# Zawartości napisu nie da się zmienić, to nie są tablice takie jak w C. str is immutable
# napis[7] = 'K'
print()

if 'm' in napis:
	print('Jest literka m')
else:
	print('Nie ma literki m')

# Dla napisów operator in sprawdza czy napis jest fragmentem dużego napisu (a nie tylko czy litera jest elementem)
if 'kot' in napis:
	print('kot obecny')
else:
	print('nie ma kota')

print('kot jest na pozycji', napis.index('kot'))
print('kot jest na pozycji', napis.find('kot'))
# Gdy nie znajdą: index wyrzuca wyjątek, a find zwraca -1
print('pies jest na pozycji', napis.find('pies'))
print()

# Napisy można dodawać - wynikiem jest nowy napis
nowy = napis + ' oraz psa'
print('nowy napis:', nowy)
print('stary napis:', napis)

# Napisy można mnożyć przez liczbę całkowitą - oznacza powtózenie treści
print('Ala ma kota. ' * 10)
print()

# Napisy są "niemutowalne", czyli nie da się zmienić zawartości obiektu typu str.
# Można natmiast do mziennej wpisać inny napis.
a = 'Ala'
b = a
print('a:', a, 'b:', b)
a += ' ma kota'
print('a:', a, 'b:', b)
# a operacje takie jak upper, lower, replace itd nie modyfikują stringa wewnątrz, tylko tworzą i zwracają nowy obiekt
a.replace('ma', 'posiada')
print('a:', a, 'b:', b)
c = a.replace('ma', 'posiada')
print('c:', c)
print()

########

# W Pythonie napisy można podawać w "cudzysłowach" albo w 'apostrofach'
napis = "Ola ma psa"
print(type(napis))
print(napis)

napis = 'Ala ma "kota" a Ola ma \'psa\''
print(napis)
print()

# Napis rozciągający na wiele linii można wpisać za pomocą
# potrójnych znaczków ''' lub """
# Często używa się tego jako komentarzy lub dokumentacji (docstring), ale jest to także normalny napis.

tekst = '''Litwo, 'ojczyzno' moja
ty jesteś jak zdrowie'''

print(type(tekst))
print(tekst)
print()

def funkcja(a,b):
	'''
	Funkcja dodaje dwie liczby
	:param a: pierwsza liczba
	:param b: druga liczba
	:return: suma liczb a i b
	'''
	return a + b

wynik = funkcja(5, 10)
print('Dokumentacja tej funkcji:', funkcja.__doc__)

# Jesli chcemy mieć tekst w jednej linii, ale w kodzie programu go podzielić,
# to w ten sposób:
tekst = 'Ala ma kota, ' \
	+ 'a Ola ma psa.'
print(tekst)

tekst = ('Ala ma kota, ' +
		'a Ola ma psa ')
print(tekst)

# Napisów umieszczonych obok siebie nie trzeba nawet łączyć znakiem +, bo Python sam je połączy
tekst = ('Ala ma kota, '
		'a Ola ma psa ' "i chomika")

print(tekst)
print()

# W niektórych sytuacjach w Pythonie używa się specjalnych wersji napisu z magiczną literą na początku.

# f-string - do wklejania i formatowania wartości
ile = 7
print(f'Ala ma {ile} kotów')
print()

# raw-string - aby znaki specjalne nie były przetwarzane.
# Najczęstsze zastosowania: wyrażenia regularne, ścieżki do plików.

# np. w normalnym napisie \t zamienia się w tabulator, \n w znak nowej linii,
# \" i \' w cudzysłów i apostrof, a \\ oznacza pojedynczy \
zwykly = 'Ala\tma\tkota \'Filemona\'\nOla\tma\tpsa\\ \"Burka\", \w wydaje na niego 15\u20ac\n'
print('zwykły', type(zwykly), len(zwykly))
print(zwykly)
print()

print('Natomiast te backslashe się wypiszą: \w\s')

# W surowym stringu (raw-string) te specjalne ciągi są traktowane jak normalna zawartość stringa.
surowy = r'Ala\tma\tkota \'Filemona\'\nOla\tma\tpsa\\ \"Burka\", \w wydaje na niego 15\u20ac'
print('surowy', type(surowy), len(surowy))
print(surowy)
print()

# Zastosowania: ścieżki do plików, wyrażenia regularne

# W Pythonie 2 napisy Unicodowe należało wpisywać w u-stringi
# u'Zażółć gęślą jaźń'


# Operacje str

lista = ['Ala', 'Ola', 'Ela']
napis = ';'.join(lista)
print(napis)
print('Witamy osoby ' + ' oraz '.join(lista) + ".")

napis = 'Ala ma kota, a Ola ma psa. Pomagamy zwierzakom.'
print(napis)

print(napis.replace('ma', 'posiada'))

napis = '   Ala ma kota, a Ola ma psa.  '
print(napis.replace(' ', '_'))

print(napis.upper())
print(napis.lower())
print(napis.strip())
print('abcd. efg'.capitalize())
print('abcd efg opr'.title())
print(napis.split())
print(napis.split(','))
