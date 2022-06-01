miasta = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań']
print(miasta)

# list comprehension - jedolinijkowe utworzenie nowej listy na podstawie innej kolekcji (lub innego źródła danych)

dlugosci_nazw = [len(miasto) for miasto in miasta]
print(dlugosci_nazw)

# to jest równoważne takiej pętli:
dlugosci_nazw2 = []
for miasto in miasta:
    dlugosci_nazw2.append(len(miasto))
print(dlugosci_nazw2)
print()

# Stwórz listę, która zawiera pierwsze litery każdego miasta
pierwsze_litery = [miasto[0] for miasto in miasta]
print(pierwsze_litery)
print()

# Można używać wiele razy for i if
# Najczęściej wyrażenia są pisane jednolinijkowo, ale gdyby była potrzeba, można dowolnie sformatować, bo jesteśmy w obrębie nawiasów
duze_litery = [miasto.upper() for miasto in miasta if miasto.startswith('W')]
print(duze_litery)

# w formie pętli byłoby tak:
duze_litery2 = []
for miasto in miasta:
    if miasto.startswith('W'):
        duze_litery2.append(miasto.upper())
print(duze_litery2)
print()

# Żródłem danych może być dowolna rzecz, dla której zadziała pętla for, dowolne "iterable"
# Bardzo często używa się range

parzyste = list(range(0, 100, 2))
print(parzyste)

parzyste = [x for x in range(0, 100, 2)]
print(parzyste)

parzyste = [2*x for x in range(50)]
print(parzyste)

# wyniki comprehencji można przekazywać od razu do funkcji takich jak sum
# uwaga - to nie jest optymalny zapis - wyjaśnienie dalej w sekcji o generatorach
suma_nieparzystych = sum([2*x+1 for x in range(10)])
print(suma_nieparzystych)

# można wprowadzić kilka zmiennych w kilku forach
tabliczka = [x*y for x in range(1,11) for y in range(1,11)]
print(tabliczka)
print('Suma wszystkich liczb tabliczki mnożenia:', sum(tabliczka))
print()

tabliczka2d = [[x*y for x in range(1,11)] for y in range(1,11)]
print(tabliczka2d)
print()


# Analogicznie: istnieją też set-comprehentions, dict-comprehentions
print(list(range(-5, 6)))

lista = [x*x for x in range(-5, 6)]
print(type(lista))
print(lista)

zbior = {x*x for x in range(-5, 6)}
print(type(zbior))
print(zbior)

generator = (x*x for x in range(-5, 6))
print(type(generator))
print(generator)
# Generator nie wylicza swoich wartości od razu i nie zawiera ich w sobie (jak lista),
# jest tylko przepisem na to jak wyliczać wartości gdy będą potrzebne
for y in generator:
    print(y, end=' ')
print()

# Dla słowników zapis jest taki:
# {klucz : wartosc for skąd się biorą...}
slownik = {x : x*x for x in range(-5, 6)}
print(type(slownik))
print(slownik)

slownik_miast = {m: len(m) for m in miasta}
print(slownik_miast)

print('\n========\n')


# Tego typu zadanko
suma_nieparzystych = sum([2*x+1 for x in range(10)])
print(suma_nieparzystych)

# może zostać zrealizowane bardziej wydajnie za pomocą generatora
# bo gdy użyjemy generatora, Python nie musi tworzyć w pamięci listy
# do funkcji sum można przekazać wyrażenie bez dodatkowych nawiasów
suma_nieparzystych = sum(2*x+1 for x in range(10))
print(suma_nieparzystych)

suma_tabliczki = sum(x*y for x in range(1,11) for y in range(1,11))
print('Suma liczb z tabliczki mnożenia:', suma_tabliczki)

print()
print('Jakie różne liczby występują w tabliczce mnożenia i ile ich jest')
print(len({x*y for x in range(1,11) for y in range(1,11)}))
print({x*y for x in range(1,11) for y in range(1,11)})
print()

# Inny przykład
# Załóżmy, że chcę stworzyć listę zawierającą kolejne potęgi dwójki od 2**0 do 2**64
# Mogę napisać tradycyjną pętlę i dodawać elementy na koniec listy...
potegi1 = []
for i in range(65):
    potegi1.append(2**i)
print(potegi1)
print()

# ... ale w Pythonie można to zrobić sprytniej:
# [wartość for x in ... ]
potegi2 = [2**i for i in range(65)]
print(potegi2)
print()
