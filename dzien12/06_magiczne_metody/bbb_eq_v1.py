class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko}'

# Jeśli w klasie nie ma zdefiniowanej metody eq, to porównanie == sprawdza
# czy po obu stronach znaku == znajduje sięten sam obiekt.

a = Osoba('Ala', 'Kowalska')
b = Osoba('Ala', 'Kowalska')
c = Osoba('Ola', 'Kowalska')
r = a

print(a == b)
print(a == c)
print(a == r) # Zmienna r wskazuje na ten sam obiekt, co zmienna a
print()

# Tam samo działa is
print(a is b)
print(a is c)
print(a is r) # Zmienna r wskazuje na ten sam obiekt, co zmienna a


