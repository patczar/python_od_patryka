# W Pythonie istnieje wiele sposobów deklarowania i przekazywania parametrów do funkcji.

# 1) Normalne parametry pozycyjne.
def aaa(a, b, c):
	print(f'aaa: a={a}, b={b}, c={c}')

# Podczas wywołania trzeba przekazać wszystkie te parametry w takiej kolejności, w jakiej zostały zadeklarowane.
aaa('Ala', 'Basia', 'Celina')

# aaa('Ala', 'Basia')
# aaa('Ala', 'Basia', 'Celina', 'Dorota')

# 2) Podczas wywołania parametry można też przekazywać po nazwie (keyword arguments):
aaa(a='Alicja', b='Barbara', c='Czesław')
# aaa(a='Alicja', bee='Barbara', cee='Czesław')

# Wówczas kolejność parametrów można zmienić
aaa(b='Bolek', c='Czarek', a='Adrian')

# Można kilka pierwszych parametrów podać pozycyjnie, a kilka kolejnych wg nazwy:
aaa('Ala', c='Celina', b='Bożena')

# aaa(b='Bożena', 'Ala', 'Celina')
print()
#########

# 3) W deklaracji funkcji można podać domyślne wartości parametrów.
# Można dla wszystkich, albo tylko dla pewnej części. Jeśli podajemy domyslne wartości dla niektórych parametrów,
# to muszą to być parametry na końcu.
# Parametry z domyślną wartością / parametry opcjonalne.

def bbb(a, b, c='Celina', d='Dorota', e='Elżbieta'):
	print(f'bbb: a={a}, b={b}, c={c}, d={d}, e={e}')

bbb('Ala', 'Basia', 'Cezary', 'Donald', 'Eliza')

bbb('Ala', 'Basia', 'Cezary')

# źle - trzeba podać wszystkie wymagane parametry
# bbb('Ala')
# za dużo to też źle
# bbb('Ala', 'Basia', 'Celina', 'Dorota', 'Elżbieta', 'Franek')

# Jeśli wywołując podamy paramatry wg nazwy, to mamy możliwość
# pominięcia parametru który jest gdzieś w środku, a podania parametru który jest dalej, np. ostatniego.

bbb('Alicja', 'Barbara', e='Eleonora')

# Np. open('plik.txt', encoding='UTF-8')

# None to nie to samo. Zostanie normalnie wczytany przez funkcję
bbb('Alicja', 'Barbara', c=None, d=None, e='Eleonora')

bbb(e='Eleonora', a='Agata', b='Balbina', d='Dziadek')

# Muszę jednak podać wszystkie te, które nie mają wartości domyślnych
#ERR bbb(e='Eleonora', b='Balbina', d='Dziadek')

# def bbbb(a, b='Barbara', c, d='Dorota', e='Elżbieta'):
# 	print(f'bbb: a={a}, b={b}, c={c}, d={d}, e={e}')


print()

# 4) Jeśli w deklaracji funkcji użyjemy parametru z pojedynczą gwiazdką,
# to przechwyci on wszystkie parametry pozycyjne podane w momencie wywołania,
# które nie dopasowały się do normalnych parametrów.

def ccc(*args):
	print(f'ccc: args={args}')
	print(f'   typem parametru jest {type(args)}, a długość = {len(args)}')
	print('Element zerowy:', args[0])
	print('----')

#ccc() # to też OK, tylko nie zadziałałoby args[0]
ccc('Jeden')
ccc('Ala', 'Basia', 'Celina')
ccc('Ala', 'Basia', 'Celina', 'Dorota', 'Eliza', 'Fela', 'Grażyna')
ccc('napis', 3.14, [3,2,1], None, 44)
print()

def proba_modyfikacji(*args):
	# args[0] = 'cośnowego'
	przekazana_lista = args[1]
	przekazana_lista.append(33)
	print('hahaha')

lista = [10,20]
print('lista', lista)
proba_modyfikacji('cokolwiek', lista, 'cośinnego')
print('lista', lista)
print()

# Parametr nie musi nazywać się args - ale taka jest konwencja.
# Przykład zastosownia (type hint przy parametrze z gwiazką dotyczy typu elementu/pojedynczego parametru)
def suma(*liczby:int):
	s = 0
	for x in liczby:
		s += x
	return s

print( suma(1,2,3) )
print( suma(1,3,5,7,9) )
print( suma() )
print()

# Parametr z gwiazdką może być podany tylko jeden i tylko po wszystkich parametrach pozycyjnych

def ddd(a, b, c='Celina', *args):
	print(f'ddd: a={a}, b={b}, c={c}, args={args}')

ddd('Ala', 'Basia', 'Cezary', 'Darek', 'Edek')

def eee(a, b, *args, c='Celina'):
	print(f'eee: a={a}, b={b}, c={c}, args={args}')

eee('Ala', 'Basia', 'Cezary', 'Darek', 'Edek')

# Jeśli funkcja ma zadkelarowane jakieś parametry za parametrem *args,
# to da się je przekazać wyłącznie po nazwie.
eee('Ala', 'Basia', c='Cezary')

# tutaj Ala i Basia są przekaza jako "positional arguments"
# natomiast Cezary jako "keyword argument"

# Tak właśnie działa print
def my_print(*args, end='\n', sep=' '):
	print('--- myprint: ---')
	print(*args, sep=sep, end=end)
	print('----------------')

my_print('Ala', 'ma', 'kota')
my_print('Ola', 'ma', 'psa', end='!', sep=',')


# Właśnie tak działa print: parametry end oraz sep można przekazać tylko po nazwie
# print('ala', 'ola', end=';', sep=',', file=plik_wynikowy)


def fff(a, b, *args, c, d='Dorota'):
	print(f'fff: a={a}, b={b}, c={c}, args={args}')

fff('Adrian', 'Bolek', 'Cezary', 'Duduś', c='Czesław', d='Dariusz')
#ERR fff('Adrian', 'Bolek', 'Cezary', 'Duduś', 'Czesio', 'Darek')

print()

# 5)
# Parametr z dwiema gwiazdkami - tradycyjna nazwa **kwargs
# - przechwytuje wszystkie parametry w wywołaniu podawane z nazwami,
# które nie były jawnie zadeklarowane wcześniej.

def ggg(**kwargs):
	print(f'kwargs: {kwargs}')
	print(f'	typem kwargs jest {type(kwargs)}')


# Ta funkcja nie przyjmie parametrów pozycyjnych
# ggg('Ala', 'Ola')

ggg(a='Ala', k='Kasia', x=113)
ggg()
print()

# Można wszystkie techniki połączyć. Konwencja Pythona: argumenty specjalne nazywają się *args i **kwargs
def hhh(a, b='Baba', *args, **kwargs):
	print('a:', a)
	print('b:', b)
	print('args  :', args)
	print('kwargs:', kwargs)
	print()


hhh('Ala', 'Basia', 'Celina', 'Dorota', 'Ela', 'Felicja')
hhh(a='Ala', b='Basia', c='Celina', d='Dorota', e='Ela', f='Felicja')
hhh('Ala', 'Basia', 'Celina', 'Dorota', e='Ela', f='Felicja')
hhh('Ala')
hhh('Ala', d='Dorota', e='Ela', f='Felicja')
hhh('Ala', d='Dorota', e='Ela', f='Felicja', b='Bożena')
print()

# 6) notacji "gwiazdkowej" można też użwać podczas wywoływania funkcji

def iii(*args):
	print(f'iii {args}')

iii('Ala', 'Basia', 'Celina')
lista = ['Alicja', 'Barbara', 'Celina', 'Dagmara']
#iii(lista) # lista byłaby pierwszym elementem tupli args
iii(*lista) # elementy wzięte z listy zostały wstawione do args

# Nawet jeśli funkcja przyjmuje "normalne paramenty",
# to w momencie wywołania można przekazać listę wartości (pisząc *lista)
# a Python sobie wyciągnie elementy z tej listy.
def jjj(a, b, c, d='Dorota', e='Eliza'):
	print(f'jjj: a={a}, b={b}, c={c}, d={d}, e={e}')

lista = ['Alicja', 'Barbara', 'Celina', 'Dagmara']
jjj(*lista)
# w tym przypadku to jest równoważne
jjj(lista[0], lista[1], lista[2], lista[3])
jjj('Alicja', 'Barbara', 'Celina', 'Dagmara')

# też OK jjj('Ala', *lista)


# To samo ze słownikiem:
slownik = {'a': 'Adam', 'b':'Bolesław', 'c':'Cezary', 'e':'Edward'}
jjj(**slownik)

# w tym przypadku to jest równoważne
jjj(a=slownik['a'], b=slownik['b'], c=slownik['c'], e=slownik['e'])

# Gdyby słownik zawierał nieoczekiwane argumenty, to spowoduje to błąd.
# (chyba że funkcja ma wpisane **kwargs)
# slownik = {'a': 'Adam', 'b':'Bolesław', 'c':'Cezary', 'e':'Edward', 'z':'Zenon'}
# jjj(**slownik)
