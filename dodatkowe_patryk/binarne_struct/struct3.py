import struct

format_naglowka = 'i'
format_rekordu = '20sii'
kodowanie = 'UTF-8'

dl_naglowka = struct.calcsize(format_naglowka)
dl_rekordu = struct.calcsize(format_rekordu)
print('Rozmiar nagłówka:', dl_naglowka)
print('Rozmiar rekordu:', dl_rekordu)

with open('towary.dat', mode='rb') as plik:
    (ilosc,) = struct.unpack(format_naglowka, plik.read(dl_naglowka))
    print('Liczba rekordów:', ilosc)
    for i in range(ilosc):
        rekord = struct.unpack(format_rekordu, plik.read(dl_rekordu))
        nazwa = rekord[0].decode(kodowanie).strip('\x00')
        print(f'Rekord nr {i}: {nazwa} za {rekord[1]}, {rekord[2]} sztuk na magazynie.')
