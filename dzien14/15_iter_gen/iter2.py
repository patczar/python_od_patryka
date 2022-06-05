class IteratorParzystych:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __next__(self):
        if self.current > self.stop:
            # sygnał dla Pythona, że należy zakończyć iterację
            raise StopIteration
        try:
            return self.current
        finally:
            self.current += 2


class Parzyste:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return IteratorParzystych(0, self.limit)


obiekt = Parzyste(100)
for x in obiekt:
    print(x)
print('koniec pętli\n')

# druga iteracja działa, bo z tego samego obiektu Parzyste ponownie pobierany jest IteratorParzystych
for x in obiekt:
    print(x)
print()
print()

# Technicznie działa to tak, że najpierw pobierany jest iterator
obiekt2 = Parzyste(20)
it = obiekt2.__iter__()
print(it)

# a następnie, dopóki nie nastapi wyjątek StopIteration, powtarzane jest pobieranie następnego elementu za pomocą next
try:
    while True:
        element = it.__next__()
        print(element, end=', ')
except StopIteration:
    print('\nKoniec\n')

# Jeśli faktycznie chcemy bezpośrednio wykonywać operacje na iteratorach, to "ładniej" jest robić to za pomocą globalnych funkcji Pythona
it = iter(obiekt2)
print(it)
try:
    while True:
        print(next(it), end='; ')
except StopIteration:
    print('\nKoniec\n')

# Ale zdecydowanie częściej używa się pętli for.
