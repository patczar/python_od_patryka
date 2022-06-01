import struct
from collections import namedtuple

format_naglowka = 'i'
format_rekordu = '20sii'
kodowanie = 'UTF-8'

dl_naglowka = struct.calcsize(format_naglowka)
dl_rekordu = struct.calcsize(format_rekordu)
print('Rozmiar nagłówka:', dl_naglowka)
print('Rozmiar rekordu:', dl_rekordu)

Towar = namedtuple('Towar', ['nazwab', 'cena', 'stan'])
towary = []

with open('towary2.dat', mode='rb') as plik:
    (ilosc,) = struct.unpack(format_naglowka, plik.read(dl_naglowka))
    print('Liczba rekordów:', ilosc)
    for i in range(ilosc):
        towar = Towar(*struct.unpack(format_rekordu, plik.read(dl_rekordu)))
        #print(towar)
        towary.append(towar)

ZMIANA = 100
towary = [towar._replace(cena = towar.cena + ZMIANA) for towar in towary]

with open('towary2.dat', mode='wb') as plik:
    plik.write(struct.pack(format_naglowka, len(towary)))
    for towar in towary:
        print(towar)
        plik.write(struct.pack(format_rekordu, *towar))

print('Gotowe')
