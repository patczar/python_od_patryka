import struct

# Tutaj cały plik zawiera jeden rekord

with open('towar.dat', mode='rb') as plik:
    bajty = plik.read()

print(f'Odczytalem {len(bajty)} bajtów')
print(bajty)
print()

format_rekordu = '20sii'
wynik = struct.unpack(format_rekordu, bajty)

print(wynik)
print(type(wynik))
print(type(wynik[0]), type(wynik[1]))

nazwa = wynik[0].decode('UTF-8')
print(nazwa)
