
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        return self.wiek >= 18

    # Standardowym sposobem na pobieranie tekstowej reprezentacji obiektu jest metoda __str__
    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    # Python przewiduje też metodę __repr__ , która zwraca tekstową ostać obiektu,
    # ale zadziała, gdy wkleimy ją do kodu źródłowego.
    # Powinno być to wyrażenie, które tworzy obiekt taki sam jak self.
    def __repr__(self):
        return f'Osoba({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)})'


a = Osoba('Ala', 'Kowalska', 30)
b = Osoba(imie='Ola', nazwisko='Malinowska', wiek=40)

# tutaj Python skorzysta z metody __str__
print(a)
print(b)
print()

print('Wyniki str:')
# tutaj Python skorzysta z metody __str__
print(str(a))
print(str(b))
print()

print('Wyniki repr:')
# tutaj Python skorzysta z metody __repr__
print(repr(a))
print(repr(b))
