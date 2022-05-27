from klasy7 import *

lista = [
    Osoba('Ala', 'Kowalska', 30),
    Student('Adam', 'Nowak', 20, rok=1, kierunek='medycyna'),
    Osoba('Ola', 'Malinowska', 40),
    Pracownik('Jan', 'Kowalski', 50, 'kierowca', 3500),
]

for o in lista:
    print(f'Kolejna osoba: {o.imie} {o.nazwisko}')
    print(o)
    o.przedstaw_sie()
    # Nie każda osoba posiada pole pensja.
    # To byłby bład: print(o.pensja)
    # Jednak gdy pracownik się przedstawia, to podaje swoją pensję.

    # Jak sprawdzić czy obiekt jest pewnej konkretnej klasy?
    print('Obiekt jest klasy', o.__class__)
    if isinstance(o, Student):
        print('To jest student kierunku', o.kierunek)
    print('---------\n')
