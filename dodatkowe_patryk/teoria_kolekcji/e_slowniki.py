# Słowniki służą do przechowywania par klucz -> wartość
# Umożliwiają łatwy i szybki dostęp do elementów po ich kluczu
# Są mutowalne (można zmieniać zawartość)
# Klucze nie mogą się powtarzać.
# Zalecane jest, aby klucze były wartościami, które łatwo jest porównywać, i które są "niemutowalne".
# Najczęściej kluczami są napisy, ale poprawne byłyby też np. int-y

slownik = {'Ala': 30, 'Ola': 40, 'Ela': 40}
print(slownik)
print(slownik['Ala'])
slownik['Ala'] += 1
print(slownik)

# dodanie nowego elementu do słownika wygląda po prostu tak:
slownik['Ula'] = 25
print(slownik['Ula'])
print(slownik)

# aktualizacja istniejącej wartości wygląda dokładnie tak samo
slownik['Ula'] = 27
print(slownik['Ula'])
print(slownik)

kto = 'Ala'
wiek = slownik[kto]
print(f'Osoba {kto} ma {wiek} lat')
print()

# Można to wykorzystać np. tak:
for kto in ['Ala', 'Ola']:
    print(f'Osoba {kto} ma {slownik[kto]} lat')
print()


# Pusty słownik
pusty_slownik_1 = {}
pusty_slownik_2 = dict()
print(pusty_slownik_1, type(pusty_slownik_1))
print(pusty_slownik_2, type(pusty_slownik_2))
print()

cennik = {'pralka': 1900, 'czajnik': 280, 'odkurzacz': 280}

print(cennik['odkurzacz'])

# kluczami nie muszą być zawsze stringi - może być coś innego, np. liczby
dni_tygodnia = {
    1: "poniedziałek",
    2: "wtorek",
    3: "środa",
    4: "czwartek",
    5: "piątek",
    6: "sobota",
    7: "niedziela",
}

print(cennik)
print(dni_tygodnia)
print(len(dni_tygodnia))
print()

# Słownik jest zoptymalizowany pod kątem szybkiego i wygodnego dostępu do danych poprzez klucz.

# Klucze powinny być obiektami porównywalnymi (mieć dobrze zdefiniowane operacje eq i hash)
# i niemutowalymi (stan klucza nie może się zmieniać w trakcie życia słownika, bo inaczej nie znajdziemy elementów które wcześniej wstawiliśmy)

# W praktyce najczęściej kluczami są napisy (str), czasami liczby całkowite (ale nie floaty),
# daty, mogą być też tuple złożone z takich typów lub nasze własne klasy po odpowiednim przygotowaniu.

# Wartości mogą być dowolnych typów.
# Czasami są to pojedyncze wartości (liczby, napisy), czasami rozbudowane obiekty (Towar, Faktura), a czasami inne kolekcje (np. listy).
szkolenia_w_miastach = {
    'Warszawa': ['Java', 'Python', 'SQL', 'Excel'],
    'Wrocław': ['Python'],
    'Kraków': ['Java', 'PHP'],
    'Poznań': [],
}

# Sprawdzanie czy podany klucz jest zdefiniowany w słowniku:
# wygodne i wydajne
print('pomidor' in cennik) # False
print('czajnik' in cennik) # True

# Sprawdzenie czy podana wartość należy do wartości słownika można zrobić tak,
# ale trzeba sobie zdawać sprawę, że to jest mało wydajne (Python musi w pętli przejrzeć całą kolekcję)
print(1900 in cennik.values())
print()

# Odczyt elementu wg podanego klucza:
# 1) indeksowanie - składnia przypominająca korzystanie z list
print('Odkurzacz kosztuje', cennik['odkurzacz'])
cennik['odkurzacz'] = 333
cennik['odkurzacz'] += 2
print('Odkurzacz kosztuje', cennik['odkurzacz'])

# przy okazji: gdy w f-stringu chcemu odczytać coś z klucza tekstowego, to przydają się dwa rodzaje cudzysłowów
print(f'czajnik kosztuje {cennik["czajnik"]}')

# Jeśli próbujemy odczytać coś z klucza, który nie był wpisywany, to dojdzie do wyjątku KeyError
#ERR print(cennik['pomidor'])
print()
for towar in ['pralka', 'pomidor']:
    if towar in cennik:
        print(f'{towar} kosztuje {cennik[towar]}')
    else:
        print(f'Towaru {towar} nie ma w cenniku')
print()

# ten sam zapis:  slownik[klucz] = nowa_wartosc
# może być użyty zarówno do wpisania nowej wartości (pod nowy klucz)
# jak i do nadpisania istniejącej wartości (gdy klucz już istniał)
print(cennik)

cennik['kuchenka'] = 2499
print(cennik)

cennik['pralka'] = 1813
print(cennik)
print()

# print(cennik['pomidor']) - bład KeyKerror

# 2) metoda get
# działa tak jak odczyt za pomocą []
# ale jeśli danego klucza nie ma w słowniku, to zwraca None, a nie wyjątek

print(cennik.get('pralka')) # 1813
print(cennik.get('pomidor')) # None

# Można też podać wartość domyślną, która ma być użyta w przypadku braku danych
print(cennik.get('pralka', 0)) # 1813
print(cennik.get('pomidor', 0)) # 0
print()

for towar in ['pralka', 'pomidor']:
    print(f'Pod kluczem {towar} jest wartość {cennik.get(towar)}')
print()

# Jak przejrzeć zawartość całego słownika?

# Domyślnie pętla for dla słownika przegląda wszystkie klucze
for towar in cennik:
    print(towar)
print()

# Jak dostać się do wartości pod kluczami?
# 1) wersja mniej wydajna: za każdym razem odczytaj spod klucza:
for towar in cennik:
    print(towar, cennik[towar])
print()

# 2) wersja bardziej wydajna: przeglądami wpisy jako pary
# for k, v in slownik.items():
# 	print('klucz:', k, 'wartość:', v)

print(cennik.items())

for towar, cena in cennik.items():
    print(towar, cena)
print()

# W sumie istnieją trzy podobne metody, które ze słownika tworzą "kolekcję czegoś"
# items() zwraca kolekcję par (klucz, wartość)
# keys() zwraca same klucze
# values() zwraca same wartości

for towar in cennik.keys():
    print('Istnieje towar', towar)
print()

for cena in cennik.values():
    print('Jakiś towar ma cenę', cena)
print()

# Poza wykorzystaniem w pętli for, można też w ten sposób utworzyć kolekcję samych kluczy lub samych wartości:

lista_towarow = list(cennik.keys())
print(lista_towarow)

posortowane_dni_tygodnia = list(dni_tygodnia.values())
posortowane_dni_tygodnia.sort()
print(posortowane_dni_tygodnia)
print()


# Można wyróżnić trzy najważniejsze zastosowania słowników w Pythonie:

# 1) "baza danych w pamięci"
# po prostu pamiętamy zestaw danych w taki sposób, aby łatwo odczytywać dane wg klucza
cennik = {'pomidor': 4.50, 'marchewka': 2.90}

# Jeśli dodatkowo mamy klasę albo coś zbliżonego do klasy,
# to wartościami mogą być obiekty
from collections import namedtuple
Towar = namedtuple('Towar', ['nazwa', 'cena', 'vat', 'stan'])
cennik2 = {
    'pral': Towar('Pralka Amica', 2800.99, 0.23, 13),
    'lod': Towar('Lodówka Electrolux', 3333.0, 0.23, 10),
    'czaj': Towar('Czajnik Philips', 300, 0.08, 50),
}

print('Dane lodówki:', cennik2['lod'])
print('Cena lodówki:', cennik2['lod'].cena)
print()

# 2) "namiastka obiektu" - takich rzeczy ze słownikami nie robi się np. w Javie,
# ale w Pythonie bardzo często, m.in. gdy obsługuje się format JSON
towar = {'nazwa': 'pralka', 'cena': 2199.00, 'vat': 0.23, 'stan': 100}

waluta = {'kod': 'USD',
      	'nazwa': 'dolar amerykański',
      	'kurs': 3.80,
}


# 3) realizacja pewnego typu algorytmów, gdy dokonujemy "grupowania" danych (jak GROUP BY w SQL)
# Zobaczymy w przykładach o employeesach


# Wypisać tylko 2 pierwsze "wiersze", np. tak, ale mówiąc szczerze to nie jest wydajne
# for towar, cena in list(cennik.items())[:2]:
#     print(towar, cena)
# print()

# To bardziej wydajne, ale brzydsze w zapisie
cnt = 0
for towar, cena in cennik.items():
    print(towar, cena)
    cnt += 1
    if cnt > 2:
        break
print()
