# Przykłady od Agaty ;)
import os
from datetime import datetime
from time import sleep


def debug(funkcja):
    def wrapper(*args, **kwargs):
        print(f'[debug] user:{os.getlogin()} '
            f'time:({datetime.now()}) '
            f'function:{funkcja.__name__}, '
            f'args:{args}, kwargs:{kwargs}' )
        wynik= funkcja(*args, **kwargs)
        print('czas po wykonaniu funkcji:', datetime.now())
        return wynik

    return wrapper


def dodaj1000(funkcja_do_wywolania):
    def opakowanie(*args,**kwargs):
        tmp = funkcja_do_wywolania(*args,**kwargs)
        return tmp+1000
    return opakowanie

print()


@dodaj1000
@debug
def dodaj(a,b):
    return a+b

@dodaj1000
@debug
def pomnoz(a,b=10):
    return a*b

@debug
def abc(a, b, c):
    print('Tu abc',a, b, c)
    sleep(0.5)
    print('papa...')


print(dodaj(11,22))

print(pomnoz(3,4))

abc('Ala', 'Basia', 'Celina')
