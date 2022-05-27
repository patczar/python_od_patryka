from konto import Konto, Osoba

def funkcja(a, b, c, x):
    print('Początek funkcji:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))
    print()

    b.wplata(48)
    x += 55
    a = Konto(a._numer, a._wlasciciel, a._saldo)
    a._saldo = 1033
    a._wlasciciel.imie = 'Alicja'
    # zrobiliśmy płytką kopię obiektu Konto. Powstały obiekt Konto odnosi się do tego samego obiektu Osoba jako właściciela.

    print('Koniec funkcji:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))
    print()


def main():
    a = Konto(1, Osoba('Ala', 'Kowalska'), 1000)
    b = Konto(2, Osoba('Ola', 'Malinowska'), 2000)
    c = b
    x = 5000

    print('Początek main:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))
    print()

    funkcja(a, b, c, x)

    print('Koniec main:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))


main()
