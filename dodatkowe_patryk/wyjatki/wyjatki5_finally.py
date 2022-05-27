print('Dzień dobry')

try:
    x = int(input('Podaj pierwszą liczbę: '))
    y = int(input('Podaj drugą liczbę: '))
    iloraz = x / y
    print('Wynik dzielenia:', iloraz)
except ZeroDivisionError as e:
    print(f'Dzielenie przez zero')
finally:
    print('Finally zawsze się wykona')
    # finally wykona się w każdej sytuacji:
    # 1) fragment programu w try bez błędów dojdzie do końca
    # 2) nastąpi wyjątek obsłużony w except
    # 3) nastapi wyjątek, który nie zostanie obsłużony przez te except(y)
    # 4) gdy wyjdziemy w tego fragmentu kodu w inny sposób: return, break

print('Koniec programu')
