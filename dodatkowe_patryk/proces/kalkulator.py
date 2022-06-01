from sys import stderr

while True:
    linia = input()
    if not linia:
        break
    try:
        wynik = eval(linia)
        print(wynik)
    except Exception as e:
        print(f'Błąd dla działania "{linia}":', e, file=stderr)
