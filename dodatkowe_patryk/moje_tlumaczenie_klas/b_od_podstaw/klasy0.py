# Klasa z pustą definicją
class Osoba:
    pass

# Co z taką pustą klasą (i jej obiektami) można robić?

# Tak tworzy się obiekt podanej klasy:
a = Osoba()
b = Osoba()
print('a:', a)
print('b:', b)

# Każdy obiekt posiada standardowe atrybuty i metody:
print(a.__dict__)
print(a.__str__())

# Dla każdego obiektu można też wywołać jedną z wielu predefiniowanych funkcji:
print(str(a))
print(hash(a))
print(isinstance(a, Osoba))
print()

# Ciekawostka
# Nawet gdy definicja klasy w żaden sposób nie deklaruje atrybutów,
# do obiektu można dodać atrybut (pole / zmienną w obiekcie).
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
a.wiek = 30
print('a:', a.imie, a.nazwisko, a.wiek)

# W obiekcie B tej samej klasy nie ma atrybutów imie, nazwisko.
#ERR print('b:', b.imie, b.nazwisko, b.wiek)
