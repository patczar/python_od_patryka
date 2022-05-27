from konto import Konto

def funkcja(a, b, c, x):
    print('Początek funkcji:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))
    print()

    b.wplata(48)
    x += 55
    a = b

    print('Koniec funkcji:')
    print('a:', a, id(a))
    print('b:', b, id(b))
    print('c:', c, id(c))
    print('x:', x, id(x))
    print()


def main():
    a = Konto(1, 'Ala', 1000)
    b = Konto(2, 'Ola', 2000)
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
