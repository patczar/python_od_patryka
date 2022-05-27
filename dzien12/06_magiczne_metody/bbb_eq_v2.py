class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko}'

    def __eq__(self, other):
        return self.imie == other.imie and self.nazwisko == other.nazwisko

# W tej wersji klasa posiada metodę eq , która za równe uznaje te obiekty, które mają równe wartości pól.

a = Osoba('Ala', 'Kowalska')
b = Osoba('Ala', 'Kowalska')
c = Osoba('Ola', 'Kowalska')
r = a

print(a == b)
print(a == c)
print(a == r)
print()

# Operator is zawsze sprawdza adresy (inaczej mówiąc: tożsamość obiektów, tak jak byśmy porównywali id tych obiektów)
print(a is b)
print(a is c)
print(a is r)
