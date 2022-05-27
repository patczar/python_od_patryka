# To NIE JEST przykład do naśladowania.
# On tylko pokazuje techniczne aspekty klas i wyjaśnia od podstaw jak to działa.

# W klasie można zdefiniować funkcje, na które wtedy mówi sie "metody".
# Poza szczególnym przypadkiem metod statycznych, metody posiadają pierwszy parametr self.
# Gdy metoda zostanie wywołana w taki sposób: obiekt.metoda(parametry),
# to do metody jako self przekazywany jest obiekt , a dopiero potem dalsze parametry.
class Osoba:
    def przedstaw_sie(self):
        # zakładając, że w obiekcie znajdują się atrybuty imie, nazwisko, wiek,
        # metoda może wyglądać tak:
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        return self.wiek >= 18


# W programie tworzymy przykładowe obiekty tej klasy

a = Osoba()
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
a.wiek = 30

b = Osoba()
b.imie = 'Ola'
b.nazwisko = 'Malinowska'
b.wiek = 40

# Atrybuty zostały wprowadzone. Teraz można bezpiecznie wywołać metodę
a.przedstaw_sie()
b.przedstaw_sie()

# Takie podejście jest nieporządne, bo łatwo jest utworzyć obiekt i "zapomnieć" wpisać tam atrybuty
c = Osoba()
#ERR c.przedstaw_sie()
