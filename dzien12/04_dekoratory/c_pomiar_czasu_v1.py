# W tej wersji dekorator zadziała tylko dla funkcji jednoargumentowych.

def pomiar_czasu(f):
    from datetime import datetime
    def wrapper(n):
        poczatek = datetime.now()
        wynik = f(n)
        koniec = datetime.now()
        print('czas działania:', koniec - poczatek)
        return wynik

    return wrapper

@pomiar_czasu
def petla(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma



suma = petla(1000)
print(suma)

suma = petla(1000_000)
print(suma)

petla(100_000_000)

