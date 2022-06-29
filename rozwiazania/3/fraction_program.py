from fraction import *

def main():
    print('Za chwilę podasz wartości 3 ułamków nazwanych a b c.')
    al = int(input('Podaj licznik a: '))
    am = int(input('Podaj mianownik a: '))
    a = Fraction(al, am)
    bl = int(input('Podaj licznik b: '))
    bm = int(input('Podaj mianownik b: '))
    b = Fraction(bl, bm)
    cl = int(input('Podaj licznik c: '))
    cm = int(input('Podaj mianownik c: '))
    c = Fraction(al, am)
    print()
    print(f'Utworzone ułamki: a = {a} , b = {b} , c = {c}')
    print('Podawaj wyrażenia, w których mogą występować zmienne a b c, a ja spróbuję obliczyć. Aby zakończyć, podaj pusty napis.')
    
    while True:
        expr = input(': ')
        if not expr: break
        try:
            result = eval(expr)
            print(expr, '=', result)
        except Exception as e:
            print('Błąd:', e)


if __name__ == '__main__':
    main()
