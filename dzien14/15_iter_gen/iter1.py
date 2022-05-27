# Jak wiemy, w Pythonie pętla for pozwala przeglądać listy, zbiory, linie z otwartego pliku, elementy range...

# O tym czy dany obiekt może być użyty "po prawej stronie w pętli for" decyduje to, czy ten obiekt jest "iterowalny" (iterable).
# Iterowalne są te obiekty, które posiadają metodę __iter__(), która z kolei zwraca iterator.

# Iterator to jest taki obiekt, na który można wielokrotnie wywoływać metodę __next__()
# a ta metoda zwraca wtedy kolejne elementy, które idą do pętli for.

# W tym przykładzie IteratorParzystych pełni rolę iteratora
# Parzyste to jest klasa iterowalna (tak jak iterowalna jest np. lista)
# W tym przykładzie iterator jest nieskończony.

# Gdy Python uruchamia pętlę for x in ZRODLO: , to postępuje tak:
# wywołuje ZRODLO.__iter__()
# dostaje w wyniku jakiś obiekt it
# i na tym obiekcie wielokrotnie wywołuje it.__next__()
# (aż dojdzie do wyjątku...)

class IteratorParzystych:
    def __init__(self):
        self.current = 0

    def __next__(self):
        try:
            return self.current
        finally:
            self.current += 2


class Parzyste:
    def __iter__(self):
        return IteratorParzystych()


obiekt = Parzyste()
for x in obiekt:
    print(x)
