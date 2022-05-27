# To NIE JEST przykład do naśladowania.
# On tylko pokazuje techniczne aspekty klas i wyjaśnia od podstaw jak to działa.

# W tej wersji tworzę metodę "wpisz_dane", która pozwala w jednej linii ustawić atrybuty w obiekcie.
class Osoba:
    def wpisz_dane(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        # zakładając, że w obiekcie znajdują się atrybuty imie, nazwisko, wiek,
        # metoda może wyglądać tak:
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        return self.wiek >= 18


# W programie tworzymy przykładowe obiekty tej klasy
# W tej wersji sami musimy pamiętać o wywołaniu metody wpisz_dane
a = Osoba()
a.wpisz_dane('Ala', 'Kowalska', 30)

b = Osoba()
b.wpisz_dane(imie='Ola', nazwisko='Malinowska', wiek=40)

# Atrybuty zostały wprowadzone. Teraz można bezpiecznie wywołać metodę
a.przedstaw_sie()
b.przedstaw_sie()

# Nadal łatwo jest utworzyć obiekt i "zapomnieć" wpisać tam atrybuty
c = Osoba()
#ERR c.przedstaw_sie()
