from decimal import Decimal
from sprzedaz import Transakcja

t = Transakcja('2020-03-04', 'Warszawa', 'Biedronka', 'słodycze', 'czekolada', Decimal('3.90'), 3)
print(type(t))
print(t)
print(str(t))
print(repr(t))
print()

# dostęp do pól poprzez indeksy oraz poprzez nazwy
print(t.sklep)
print(t[2])
print(t[2:5])

# obiekty są niemutowalne
#ERR t.sklep = 'Żabka'
#t[2] = 'Inny sklep'
print(t)

t._replace(miasto = 'Pruszków', cena = Decimal('5.55'))
print(t) # t się nie zmienia. replace zwraca NOWY OBIEKT

t2 = t._replace(miasto = 'Pruszków', cena = Decimal('5.55'))
print(t2)

# aby zaienić zawartość zmiennej t, trzeba tak:
# t = t._replace(...)

# Pobierz dane w postaci słownika. To jest oddzielny słownik, niepowiązany już z obiektem t
d = t._asdict()
print(d)
d['miasto'] = 'Kraków'
print(d)
print(t)

