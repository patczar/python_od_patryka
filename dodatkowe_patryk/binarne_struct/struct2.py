import struct

# W tej wersji plik na początku ma jednego inta - liczba rekordów
# a następnie wiele rekordów.
# Program wczyta cały plik do pamięci, a potem w pętli odczyta rekordy z tablicy bajtów.

format_naglowka = 'i'
format_rekordu = '20sii'
dl_naglowka = struct.calcsize(format_naglowka)
dl_rekordu = struct.calcsize(format_rekordu)
print('Rozmiar nagłówka:', dl_naglowka)
print('Rozmiar rekordu:', dl_rekordu)

with open('towary.dat', mode='rb') as plik:
    bajty = plik.read()

# Teraz nie można przekazać całej tablicy do unpack, bo jest za długa
# wynik = struct.unpack(format_naglowka, bajty)

# Można przekazać początkowy fragment
wynik = struct.unpack(format_naglowka, bajty[:4])
print(wynik)

# Lepiej będzie tu jednak użyć unpack_from, który czyta fragment od podanej pozycji
# i działa również wtedy, gdy tablica zawiera dalsze dane
ile, = struct.unpack_from(format_naglowka, bajty, 0)
print(f'W pliku jest {ile} rekordów')

pozycja = dl_naglowka
for i in range(ile):
    nazwab, cena, sztuk = struct.unpack_from(format_rekordu, bajty, pozycja)
    nazwa = nazwab.decode()
    print(f'Towar nr {i}: {nazwa} za {cena}. W magazynie {sztuk} sztuk.')
    pozycja += dl_rekordu

