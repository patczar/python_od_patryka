# Zmienna definiowana na poziomie pliku to jest "zmienna globalna"
gloobalna = 'lalala'

# także gdy jest w jakimś if-e, try-u itp.
if 5 > 0:
    globalna = 100


def aaa(a):
    # jeśli w obrębie funkcji stosujemy przypisanie wartości na zmienną,
    # a ta zmienna nie jest zadeklarowana jako global,
    # to Python przyjmuje, że jest zmienna lokalna

    # Zmienna definiowana wewnątrz funkcji, to "zmienna lokalna"
    lokalna = 50

    # odczyt zmiennych
    # własny parametr - bez problemu
    print(a)

    # zmienna lokalna - bez problemu
    print('aaa lokalna:', lokalna)

    # zmienna globalna - można czytać bez deklarowania
    # o ile wcześniej zmienna została zdefiniowana przed uruchomieniem tej funkcji
    print('aaa globalna:', globalna)

    inna1()

    print('aaa lokalna po raz drugi:', lokalna)
    print('globals:', globals())
    print('locals:', locals())

    print('koniec aaa')


def inna1() :
    print('inna1')
    # w jednej funkcji nie ma dostepu do zmiennej lokalnej innej funkcji
    # print(lokalna)


def bbb(a):
    # modyfikacja zmiennych
    # parametr - można
    a += 1
    print('bbb: parametr a = ', a)

    # lokalna - można stworzyć i modyfikować
    lokalna = 40
    lokalna += 1
    print('bbb lokalna', lokalna)

    # globalna?
    # Jeśli bez deklarowania global na zmienną o takiej samej nazwie jak jakaś zmienna globalna
    # wpiszę wartość, to tak naprawdę jest to deklaracja zmiennej lokalnej.
    # "przesłonięcie" zmiennej globalnej przez zmienną lokalną
    globalna = 500
    globalna += 1 # zmiana zmiennej lokalnej o nazwie "globalna"
    print('bbb globalna', globalna) # tak naprawdę zmienna lokalna tej funkcji
    print('globals:', globals())
    print('locals:', locals())
    print('koniec bbb')


def ccc():
    # Jeśli nie deklarując global próbuję
    # najpierw odczytać zmienną globalną
    print(globalna)

    # A następnie zapisać / zmienić
    globalna = 500
    globalna += 1

    print(globalna)

    # To już przy oczycie pojawia się błąd
    # local variable 'globalna' referenced before assignment


def ddd():
    # Jeśli wewnątrz funkcji świadomie chcemy modyfikować zmienną globalną,
    # to musmy ją zadeklarować pisząc global

    global globalna
    global nowa_globalna
    nowa_globalna = 641
    # global x, y, z

    print('ddd globalna', globalna)
    print('ddd zmienia globalną')

    globalna = 700
    globalna += 1

    print('ddd globalna', globalna)
    print('koniec ddd')


globalna = 200
print('program globalna', globalna)
aaa(33)
#ERR print('lokalna odczytywana w programie:', lokalna)
print()

print('program globalna', globalna)
bbb(44)
print('program globalna', globalna)
print()

# błąd gdy uruchomimy
# ccc()

ddd()
print('program globalna', globalna)
print('nowa globalna:', nowa_globalna)
print()


# globalne x i y = 100
x = 100
y = 100

def ggg():
    # Tutaj widzimy zmienne globalne, a nie zmienne z fff, chociaż fff wywołał ggg
    print('ggg x = ', x, ', y = ', y)

def fff(x):
    y = 2*x
    print('fff x = ', x, ', y = ', y)
    x += 1
    print('fff x = ', x, ', y = ', y)
    ggg()
    print('fff x = ', x, ', y = ', y)
    print('koniec fff')

fff(44)
print()

globalna_lista = ['oryginał']
def eee():
    # modyfikacja obiektu "w środku" to nie jest to samo co zapisanie zmiennej
    # formalnie rzecz biorąc, my tutaj zmienną globalną odczytujemy, a de facto możemy zmodyfikować bez piosania global
    globalna_lista[0] = 'podróbka'
    globalna_lista.append('nowy element')
    # zabronione jest to:
    # globalna_lista = ['nowa lista']

print('lista1', globalna_lista)
eee()
print('lista2', globalna_lista)
