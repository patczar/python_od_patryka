# Listy są mutowalne (można je zmieniać)
# Listy pamiętają kolejność elementów i można indeksować (listy są sekwencjami)

imiona = ['Ala', 'Adam', 'Iwona', 'Kasia', 'Janusz']
liczby = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
miks = [123, 'Ala', 3.14, [3,2,1]]

print(imiona)
print(liczby)

print('Liczba imion:', len(imiona))
print('Liczba liczb:', len(liczby))

# de facto to jest wywołanie takiej metody, ale "zwykły programista" powinien używać funkcji len() aby to uzyskać
print('_len:', imiona.__len__())

print()

# A tak tworzy się pustą listę (2 sposoby)
pusta1 = []
pusta2 = list()

print(pusta1, len(pusta1), type(pusta1))
print()

# Łatwo można przejrzeć wszystkie elementy lista i dla każdego coś zrobić
for imie in imiona:
    print('Kolejną osobą jest', imie)
print()

for x in liczby:
    print(x, end='; ')
print()

# W przypadku kolekcji zawierająch liczby, można skorzystać z gotowych funkcji:
print('Suma:', sum(liczby))
print('Max:', max(liczby))
print('Min:', min(liczby))

# max i min dla dowolnych typów, które da się porównywać
print('Maksymalne imię:', max(imiona))
print()

# Odczytać konkretny element listy wg jego pozycji można za pomocą [indeksowania]
print(imiona[2])
# Obowiązuje numeracja od 0

# Można uzywać indeksów ujemnych - wtedy liczymy od końca.
# -1 to ostatni element
print(imiona[-1])
# print(imiona[len-1])

# Gdy wyjdziemy poza zakres listy ( >= rozmiar  albo < -rozmiar), to będzie wyjątek IndexError
#ERR print(imiona[10])
print()

# Listy są mutowalne - zawartość list można modyfikować.

# Zmiana elementu na określonej pozycji:
print(imiona)
imiona[0] = 'Alicja'
imiona[3] = 'Katarzyna'
# ale nie da się w ten sposób wpisać na nieistniejącą pozycję
#ERR imiona[5] = 'Alojzy'
print(imiona)

# Dodanie nowego elementu na końcu:
imiona.append('Krzysztof')
print(imiona)

# Wstawienie elementu w środek. Na pozycję 3 wstaw wartość Magdalena → reszta się przesunie
imiona.insert(3, 'Magdalena')
print(imiona)

# Aby za jednym zamachem dodać wiele elementów, można uzyć extend
inna_lista = ['Zuzia', 'Adrian', 'Bożena']
imiona.extend(inna_lista)
# imiona.append(inna_lista)
print(imiona)
print()

# Listy można też dodawać za pomocą + , ale to działa podobnie jak + w matematyce
a = [1,2,3]
b = [4,5]

print('a:', a, 'b:', b)
print(a+b)
# Listy a i b nadal pozostały sobą
print('a:', a, 'b:', b)
c = a + b
print('c:', c)

# Aby w ten sposób zmodyfikować istniejącą listę, można użyć
a += b
print('a:', a, 'b:', b)
# efekt analogiczny do extend

print()
# Usunięcie elementu z określonej pozycji. Dalsze elementy przesuwają się ← w lewo
del imiona[1]
print(imiona)

# Usunięcie elementu o podanej wartości
imiona.remove('Janusz')
print(imiona)

# Próba usunięcia elementu niesitniejącego kończy się błędem
# imiona.remove('Mikołaj')
# print(imiona)

# Aby sprawdzić, czy lista coś zawiera, używamy operatora in
# Przy czym dla listy jest to kosztowne - Python musi przejrzeć całą listę
if 'Tomasz' in imiona:
    print('Lista zawiera imię Tomasz')
else:
    print('Lista nie zawiera imienia Tomasz')
print()

# Odwrócenie listy
print(liczby)
liczby.reverse()
print(liczby)
liczby.extend([33, 66, 99, 155])
print(liczby)

# Posortowanie listy
liczby.sort()
print(liczby)

print()


# Gdy korzysta się z listy jako "stosu", wtedy bardziej czytelne może być używanie operacji append i pop

l = []
l.append('Warszawa')
l.append('Kraków')
l.append('Łódź')
l.append('Wrocław')
l.append('Poznań')
print(l)
# pop usuwa ostatni element
print('3 razy pop() : ')
print(l.pop())
print(l.pop())
print(l.pop())
print(l)
l.append('Bydgoszcz')
l.append('Toruń')
print(l)

print()

print(imiona)

# Spr. czy element należy do listy
print('Katarzyna' in imiona)
kogoszukam = 'Zuzia'
if kogoszukam in imiona:
    print('Znaleziono')
else:
    print('Nie ma')

# Jeśli interesuje nas nie tylko czy obiekt należy do listy, ale także na jakiej pozycji się znajduje, używamy wtedy metody index

pozycja = imiona.index(kogoszukam)
print(f'Osoba {kogoszukam} znajduje się na pozycji {pozycja}')

# Wywołanie index dla elementu, którego nie ma w liście, kończy się wyjątkiem

# pozycja = imiona.index('Patryk')

# 2 sposoby, żeby sobie z tym poradzić:
# Podejście "defensywne"
kogoszukam = 'Patryk'
if kogoszukam in imiona:
    pozycja = imiona.index(kogoszukam)
    print(f'Osoba {kogoszukam} znajduje się na pozycji {pozycja}')
else:
    print(f'Lista nie zawiera elementu {kogoszukam}')

# Podejście "ofensywne" - dość często praktykowane w Pythonie
try:
    print(f'Osoba {kogoszukam} znajduje się na pozycji {imiona.index(kogoszukam)}')
except ValueError:
    print(f'Lista nie zawiera elementu {kogoszukam}')
print()

# Zwykła pętla for przegląda elementy listy, nie mamy informacji o pozycji
for imie in imiona:
    print(imie)
print()

# Pętla w stylu języka C przeglądająca indeksy, w Pythonie wygląda tak:
for i in range(len(imiona)):
    print(f'{i} → {imiona[i]}')
print()

# Rozwiązaniem bezpośrednio służącym do przejrzenia elementów listy wraz z ich pozycjami, jest enumerate
for i, imie in enumerate(imiona):
    print(f'{i} → {imie}')
print()

# Samo enumerate tworzy kolekcję par:
print(enumerate(imiona))
print(list(enumerate(imiona)))
# w enumerate można podać numer początkowy
print(list(enumerate(imiona, 11)))
print()


# Operacja zip na podstawie dwóch list tworzy listę par.
# Typowe zastosowanie to pętla przechodząca jednocześnie po dwóch listach.
lista1 = ['Opel', 'Toyota', 'BMW', 'Audi', 'VW', 'Fiat']
lista2 = ['Astra', 'Prius', '5', 'A6', 'Passat TDI']

for a, b in zip(lista1, lista2):
    print(a, b)
print()

# Samo zip tworzy listę par:
zipped = zip(lista1, lista2)
print(list(zipped))

slownik = dict(zip(lista1, lista2))
print(slownik)

print('Koniec programu')
