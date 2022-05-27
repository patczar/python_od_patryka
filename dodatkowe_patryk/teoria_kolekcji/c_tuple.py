# tupla, krotka
tupla = ('Ala', 'Ola', 'Ela')
print(tupla, type(tupla))

punkt = (1.25, -3.0)
print(punkt)

# tuple mogą zawierać duplikaty
# kolejność jest zachowywana
# można indeksować (lista[i], wycinanki...)
# tuple są "niemutowalne" (immutable)
print(tupla[1])
print(tupla[0:2])

# nie zadziałają:
# tupla[1] = 'Aleksandra'
# TypeError: 'tuple' object does not support item assignment
# tupla[2:3] = ('Ela', 'Ula')

# tupla.append('Ula')
# tupla.insert(2, 'Ewa')
# del tupla[1]

# Natomiast MOŻNA do istniejącej zmiennej wpisać nową tuplę:
tupla = ('Adam', 'Ludwik', 'Ksawery')
print(tupla)

# No bo w Pythonie zawsze można do zmiennej wpisać zupełnie nowy obiekt:
tupla = 'To nie jest tupla'
print(tupla)
print()

# Można też modyfikować obiekty, które znajdują się w tupli, o ile same te obiekty są mutowalne.
dwie_listy = (['Polska', 'Czechy'], ['Warszawa', 'Praga'])
print(dwie_listy)
dwie_listy[0].append('Słowacja')
dwie_listy[1].append('Bratysława')
print(dwie_listy)
print()

# pusta tupla:
pusta_tupla_1 = ()
pusta_tupla_2 = tuple()
print(pusta_tupla_1, type(pusta_tupla_1))
print(pusta_tupla_2, type(pusta_tupla_2))

# jak utworzyć tuplę jednoelementową?
# nie tak:
tupla1 = (123)
print(tupla1, type(tupla1)) # int

# tylko tak:
tupla1 = (123,)
print(tupla1, type(tupla1)) # tuple
print()

# ZASTOSOWANIA
# "Normalny programista Pythona" zdecydowanie częściej używa list
# tuple są intensywnie używane wewnętrznie przez Pythona - m.in. przekazywanie parametrów do funkcji
# tuple są używane przy realizacji różnych Pythonowych sztuczek, np. przeglądanie zawartości słowników
# przy "rozpakowywaniu", zwracaniu wielu wyników na raz itp.

# Przykład zwracania dwóch wyników na raz i ich rozpakowania
def dzielenie_z_reszta(x, y):
    return x//y, x%y

tupla_wynikowa = dzielenie_z_reszta(20, 7)
print('typ wyniku:', type(tupla_wynikowa), 'wynik:', tupla_wynikowa)
print(f'Wynik dzielenia to {tupla_wynikowa[0]} i {tupla_wynikowa[1]} reszty')

# "rozpakowywanie"
(iloraz, reszta) = tupla_wynikowa
print(f'Wynik dzielnia to {iloraz} i {reszta} reszty')

# Często można nie pisać okrągłych nawiasów
a, b = dzielenie_z_reszta(20, 7)
print(a, b)

# Inne zastosowanie - krótkie przypisanie wielu zmiennych na raz
x, y, kto = 100, 200, 'Ala'
print(x, y, kto)

# "swap" czy zamiana wartości zmiennych
x, y = y, x
print(x, y, kto)

#############

# Teoretycznie każda kolekcja może zawierać elementy różnych typów. Np. lista
lista = ['Ala ma kota', 1234, 3.14, (1,2,3), 'Koniec']
print(lista)

# W typowym zastosowaniu lista zawiera wiele jendorodnych elementów (np. same napisy, albo same liczby)
# nieograniczonej długości. Typowe jest, że do list są dodawane nowe elemente w czasie działania programu.
# Lista jest bardziej jak kolumna w Excelu
imiona = ['Ala', 'Ola', 'Ela']
imiona.append('Ula')
print(imiona)

# Tuple natomiast często zawierają dane różnych typów lub kolejne pola pełnią różną rolę.
# Zwykle tuple mają z góry znany rozmiar i wiadomo co będzie na której pozycji
# (jak w rekordzie bazodanowym, jak wiersz w Excelu)
t2 = ('Ala', 'Kowalska', 30, 'Jasna', 'Warszawa', True)
print(t2)

# Python tego nie sprawdza, ale taka jest praktyka użycia...
# To nie jest ścisłe, to tylko delikatne wskazówki, z których można się wyłamać.

# Rada: gdy nie wiemy czego użyć, użyjmy listy.
