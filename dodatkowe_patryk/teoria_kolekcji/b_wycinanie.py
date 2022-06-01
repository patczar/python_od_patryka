# Python posiada składnię "slices" ("wycinanki"),
# która pozwala w bardzo wygodny sposób wybierać fragmenty list (i innych sekwencji)

l = ['zero', 'jeden', 'dwa', 'trzy', 'cztery',
     'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
print(l)
print('len =', len(l))
print()

# Można wybierać pojedyncze elementy
print('l[0]', l[0])
print('l[3]', l[3])
print('l[9]', l[9])
# print(l[10]) # IndexError: list index out of range

# liczenie od końca
print('l[-3]', l[-3])
# ostatni
print('l[-1]', l[-1])
print('l[-1]', l[len(l)-1])
print()

# Notacją z dwukropkami wybiera się przedziały / fragmenty list

print('l[3:7]', l[3:7]) # pozycje od 3 do 6
# gdy mówimy o zakresach, to zawsze jest to zakres od lewej granicy włącznie, do prawej wyłączając
# (lewostronnie domknięty)
# przy czym numerujemy od zera

# odwołanie do pojedynczego elementu poza zakresem kończy się błędem IndexError
# print(l[20])

# wyjście poza listę w przypadku zakresu nie powoduje błędu - po prostu dostajemy krótszy fragment, czasami wręcz pusty
print('l[5:25]',  l[5:25])
print('l[20:25]', l[20:25])
print('l[-8:-6]', l[-8:-6])
print('l[2:4]', l[2:4])
print('l[-8:6]',  l[-8:6])
print('l[8:3]',  l[8:3])
print()

# trzeci parametr składni "przedziałowej" / "slices" oznacza wielkość kroku
# (domyślnie krok = 1)

print('l[2:10:2]', l[2:10:2])
print('l[0:10:3]', l[0:10:3])
print()

# Niektóre parametry można pominąć. Pierwszy to domyślnie 0, drugi to domyślnie len
print('l[::2]', l[::2]) # wypisz wszystkie pozycje parzyste

# elementy od początku do 4
print('l[:5]', l[:5])
print('l[:5:]', l[:5:]) # równoważne powyższemu

# od 5 do końca
print('l[5:]', l[5:])
print()

print('l[:]', l[:])
print('l[::]', l[::])
print()

# Gdy krok jest ujemny, to przeglądamy elementy w odwrotnej kolejności
print('l[8:2:-2]', l[8:2:-2]) # 8 6 4

# Najprostszy sposób na odwrócenie listy:
print('l[::-1]', l[::-1])
print()

# Napisy (str) też są "sekwencjami" i można do nich stosować indeksowanie i wycinanie
tekst = 'Ala ma kota a Ola ma psa'
print(tekst[2])
print(tekst[-2])
print()

# spróbujcie wyciąć słowo "kota"
print(tekst[7:11])

print(tekst[::2])

# od tyłu:
print(tekst[::-1])

print('\n' + 60*'=' + '\n')

lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Katowice', 'Białystok', 'Toruń', 'Bydgoszcz']
print(lista)

# do wstawiania elementów można też użyć zakresów:
print(lista[5])

print(lista[5:5])

lista[5:5] = ['Trójmiasto']
print(lista)

# Uwaga, inaczej zadziałałoby:
# lista[5] = ['Trójmiasto']
# print(lista)

print(lista[5:6]) # ['Trójmiasto']
# zastąp wycinek o długości jeden tymi trzema elementami
# zastępuje Trójmiasto tymi trzema miastami
lista[5:6] = ['Gdańsk', 'Sopot', 'Gdynia']
# ze słownika wzięłoby klucze
# lista[5:6] = {'GdańsK': 10, 'SopoT': 20, 'Gdynia': 30}
# trzy_miasta = ['Gdańsk', 'Sopot', 'Gdynia']
# lista[5:6] = trzy_miasta
print(lista)

# Usunie elementy Wrocław i Poznań
lista[3:6] = []
print(lista)

# Można też deletować zakresy:
del lista [1:4]
print(lista)

#txt = 'ABCDEF'
#txt[1:2] = 'XY'
