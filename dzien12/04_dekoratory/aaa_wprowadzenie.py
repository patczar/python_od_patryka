# Funkcja poczatek_i_koniec jest "funkcją wyższego rzędu", tzn.
# jako parameter przyjmuje i jako wynik zwraca inną funkcję.
# Operuje na funkcjach, a nie na zwykłych wartościach.

# Funkcja poczatek_i_koniec jako parametr przyjmuje pewną funkcję bezargumentową.
# W wyniku zwraca zmienioną funkcję, która działa tak jak f, ale dodatkowo na początku
# i na końcu swojego działania wypisuje POCZATEK i KONIEC.
def poczatek_i_koniec(f):
    def zmieniona_funkcja():
        print('POCZATEK')
        f()
        print('KONIEC')

    return zmieniona_funkcja

def powitaj():
    print('Witamy serdecznie')

def pozdrow():
    print('Na zdrowie!')


print('Normalne powitaj:')
powitaj()
print()

zmienione_powitaj = poczatek_i_koniec(powitaj)
print('Zmienione powitaj:')
zmienione_powitaj()
print()

zmienione_pozdrow = poczatek_i_koniec(pozdrow)
print('Zmienione pozdrów:')
zmienione_pozdrow()
zmienione_pozdrow()
print()

# Można też wywołać zmienioną funkcję bez wpisywania na zmienną:
poczatek_i_koniec(powitaj)()
