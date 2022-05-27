print('Hello world')

a = 'globalna A'
print('a:', a)

def funkcja1():
    b = 'lokalna B1'
    print('b:', b)
    # w obrębie funkcji można odwoływać się zarówno do zmiennych lokalnych tej funkcji, jak i do zm,. globalnych
    # dokładnie mówiąc, bez problemu można odczytać zmienną globalną
    print('a:', a)
    funkcja2()


def funkcja2():
    print('a:', a)
    #ERR print('b:', b)
    # nawet jeśli ta funkcja została wywołana przez funckja1 (gdzie była zmienna b), to tutaj zmiennej b nie widać


funkcja1()
# po zakończeniu funkcji nie ma dostępu do zmiennych lokalnych wprowadzonych w tej funkcji
# print('b:', b)

###############
print()

c = 100

def funkcja3():
    # tutaj zmienną globalną przesłaniamy za pomocą zmiennej lokalnej o tej samej nazwie
    c = 200
    print('c:', c)
    wypisz_c() # ??

def wypisz_c():
    print('globalne c = ', c)

print('c:', c)
funkcja3()
print('c:', c)


def funkcja4():
    # spróbujmy najpierw odczytać zm. globalną, a potem pod tą samą nazwę wpisać inną wartość
    # powoduje to błąd "local variable 'c' referenced before assignment"
    print(c)
    c = 300

# funkcja4()


# Jak napisać funkcję,  której celem jest zmodyfikować zmienną globalną?
# Trzeba użyć deklaracji global
def funkcja5():
    global c, a
    print('przed zmianą c =', c)
    c += 50
    a = 'Ala ma kota'
    print('  po zmianie c =', c)

print('globalne c =', c)
funkcja5()
print('globalne c =', c)
print('globalne a =', a)
print()

print(globals())

def funkcja6(param1, param2):
    c = 13
    print('Jestem w funkcja 6.')
    print('Widzę takie zmienne globalne:', globals())
    print('Widzę takie zmienne lokalne:', locals())
    print('Odczytuję globalne c z wnętrza funkcji:', globals()['c'])

funkcja6('Python', 3)

