# własna klasa wyjątku - dziedziczymy z Exception i zazwyczaj niczego nie zmieniamy
class PechowaLiczba(Exception):
    pass

def procedura1():
    try:
        x = int(input('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        if x == 33 or y == 33:
            print('Przerywam procedura1, bo 33')
            return
        print('Wchodzę do procedura2')
        procedura2(x, y)
        print('procedura2 zakończona')

    except ZeroDivisionError:
        print(f'Dzielenie przez zero!')
    except ValueError as e:
        print(f'Wystąpił ValueError {e}')
    except PechowaLiczba:
        print('A to pech...')
    except Exception as e:
        print(f'Wystąpił inny błąd typu {type(e)} : {e}')
    finally:
        print('To się zawsze wykona')
    # finally wykona się jeśli
    # 1) nie było wyjątku,
    # 2) był wyjątek i został wyłapany,
    # 3) był wyjątek i nie został wyłapany
    # 4) kiedy z tego fragmentu programu wychodzimy za pomocą return, break itp. (ale nie exit !!!)


def procedura2(x, y):
    iloraz = x / y
    print('Wynik dzielenia:', iloraz)
    if x == 13 or y == 13:
        raise PechowaLiczba('Wybrałeś pechową trzynastkę')
    print('Wszystko było OK')


print('początek programu')
procedura1()
print('Koniec programu')
