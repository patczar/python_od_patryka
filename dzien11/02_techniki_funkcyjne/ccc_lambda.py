# Funkcję w Pythonie można zdefiniować za pomocą def
# Wówczas ta funkcja jest wpisywana do zmienne globalnej o podanej nazwie
def kwadrat(x):
    return x**2

def szescian(x):
    return x**3

print(globals())
print(kwadrat(5))
print(szescian(5))

# Funkcję można teżjednak zdefiniować za pomocą "wyrażenia lambda" (lambda expression)

kw = lambda x: x**2
print(kw(5))

# Wyrażeń lambda używa się najczęściej, gdy funkcję trzeba przekazać jako parametr do innej funkcji
# lub gdy dodajemy funkcje do kolekcji

funkcje = [kwadrat,
           szescian,
           lambda arg: 10*arg,
           lambda x: x - 1
          ]

liczby = list(range(1, 6))

print(funkcje)
print(liczby)

for liczba in liczby:
    print(liczba, end=': ')
    for funkcja in funkcje:
        # print(funkcja(liczba), end=', ')
        print(f'{funkcja(liczba):3}, ', end='')
    print()
