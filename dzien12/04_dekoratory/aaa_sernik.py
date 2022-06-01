def rodzynki(przepis):
    def zmieniona_funkcja():
        przepis()
        print('I jeszcze dodaj rodzynki!')

    return zmieniona_funkcja

def sernik_klasyczny():
    print('Weź zmielony twaróg')
    print('Dodaj cukier i aromaty')
    print('Oddzielnie przygotuj ciasto')
    print('Połóż masę serową na ciasto')


# Tu wywołam orygonalną funkcję - bez rodzynek
print('Normalny przepis:')
sernik_klasyczny()
print()

# Funkcja rodzynki bierze "normalną funkcję" i zwraca nową funkcję (inną wersję),
# która na końcu wypisuje jeszcze tekst o rodzynkach.
zmieniony_przepis = rodzynki(sernik_klasyczny)
print('Zmieniony przepis:')
zmieniony_przepis()
print()

# Właśnie taka funkcja jak "rodzynki", która zmienia inne funkcje, może byc używana jako dekorator.

@rodzynki
def sernik_brzoskwiniowy():
    print('Weż masę serową')
    print('Dodaj kawałki brzoswkiń')


# Teraz pod nazwą sernik_brzoskwiniowy od razu jest wersja z rodzynkami
print('Brzoskwiniowy:')
sernik_brzoskwiniowy()
