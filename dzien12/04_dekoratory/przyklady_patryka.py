# Podmiana funkcji na zupełnie inną
def fake(*args, **kwargs):
    print('hahaha')

# Gdybyśmy chcieli, aby fake mógł być wywołany z dowolnymi parametrami, to:
# def fake(*args, **kwargs):
# 	print('hahaha')


# Prawdziwej funkcji w ogóle nie uruchamia,
# zamiast niej podstawia fake
def oszukaj(funkcja):
    return fake

@oszukaj
def bardzo_wazna_rzecz():
    print('To są bardzo poważne sprawy')
    print('itd itp')


bardzo_wazna_rzecz() # hahaha
print()

#######

# dekorator blokuje przekazywanie parametru równego 0 - w tym przypadku zgłosi wyjątek
def nie_zero(funkcja):
    def wrapper(liczba, *args, **kwargs):
        if liczba == 0:
            raise ValueError('Liczba nie może być zerem!')
        funkcja(liczba, *args, **kwargs)
    return wrapper


@nie_zero
def wplata(kwota):
    print('Wpłacam wartość ', kwota)

@nie_zero
def wyplata(kwota):
    print('Wypłacam wartość ', kwota)

@nie_zero
def wiecej_parametrow(liczba, napis, lista):
    for i in range(liczba):
        print(napis)


try:
    wplata(100)
    wyplata(50)
    wplata(0)
except Exception as e:
    print(e)
