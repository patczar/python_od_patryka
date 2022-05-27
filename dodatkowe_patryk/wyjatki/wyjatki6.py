# własna klasa wyjątku - dziedziczymy z Exception i zazwyczaj niczego nie zmieniamy
class PechowaLiczba(Exception):
    pass


print('Dzień dobry')

try:
    x = int(input('Podaj pierwszą liczbę: '))
    y = int(input('Podaj drugą liczbę: '))
    iloraz = x / y
    print('Wynik dzielenia:', iloraz)
    if iloraz == 13.0:
        raise PechowaLiczba('Wybrałeś pechową trzynastkę')

    print('Wszystko było OK')

except ZeroDivisionError:
    print(f'Dzielenie przez zero!')
except ValueError as e:
    print(f'Wystąpił ValueError {e}')
except PechowaLiczba as e:
    print('A to pech...', e)
except Exception as e:
    print(f'Wystąpił inny błąd typu {type(e)} : {e}')

print('Koniec programu')
