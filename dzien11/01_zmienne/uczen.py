'''
Utwórz klasę Uczen, które atrybutami są imie, nazwisko i lista ocen.

Listę ocen można podać od razu podczas tworzenia obiektu, ale gdy nie podamy,
to na początku Uczen ma pustą listę ocen.

Utwórz metodę dodaj_ocene , aby można było dodawać ocenę do listy ocen
i metodę srednia_ocen , które oblicza średnią

I ew. ładny str
'''

# To jest ogólny sposób obsługi domyślnych parametrów, jeśli zależy nam na tym,
# aby ta domyślna wartość (tutaj: pusta lista) była tworzym za każdym razem.
class Uczen:
    def __init__(self, imie, nazwisko, oceny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if oceny is None:
            oceny = []
        self.oceny = oceny

    def __str__(self):
        return f'Uczeń {self.imie} {self.nazwisko} z ocenami {self.oceny}'

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)


ala = Uczen('Ala', 'Kowalska', [5, 4, 5, 3])
print(ala)
print(ala.srednia_ocen())
ala.dodaj_ocene(3)
print(ala.srednia_ocen())
print(ala)
print()

jan = Uczen('Jan', 'Kowalski')
print(jan)
jan.dodaj_ocene(3)
jan.dodaj_ocene(5)
print(jan.srednia_ocen())
print(jan)
print()

adam = Uczen('Adam', 'Malinowski')
print(adam)
adam.dodaj_ocene(5)
adam.dodaj_ocene(6)
jan.dodaj_ocene(2)
print(adam.srednia_ocen())
print(adam)
