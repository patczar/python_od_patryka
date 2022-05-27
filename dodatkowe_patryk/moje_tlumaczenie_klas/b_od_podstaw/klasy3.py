# To już jest wersja w miarę poprawna...

# W tej wersji zamiast tworzyć własną metodę "wpisz_dane", używamy standardowej nazwy __init__.
# To jest właśnie metod służąca do inicjalizacji obiektów, ale ona działa w specjalny sposób.
# Python wywołuje tę metodę podczas tworzenia obiektu i przekazuje do niej parametry podane podczas tworzenia obiektu
# np. obiekt = Osoba('Ala', 'Kowalska', 30) → __init__(obiekt, 'Ala', 'Kowalska', 30)

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
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
# Teraz już trudno zapomnieć o inicjalizacji obiektu, bo Python wymaga przekazania parametrów podczas tworzenia obiektu
# Przypomina o tym również edytor np. PyCharm
a = Osoba('Ala', 'Kowalska', 30)

b = Osoba(imie='Ola', nazwisko='Malinowska', wiek=40)

# Atrybuty zostały wprowadzone. Teraz można bezpiecznie wywołać metodę
a.przedstaw_sie()
b.przedstaw_sie()

# błąd już w tym miejscu c = Osoba()

print('\n' + '-'*80 + '\n')

print(a)
print(b)

print('\n' + '-'*80 + '\n')
# Wyjaśnienie techniczne co robi Python podczas tworzenia obiektu.
# Na co dzień tak się nie programuje:
# 1. tworzę surowy, niezainicjowany obiekt
d = Osoba.__new__(Osoba)

# 2. wywołuję init
d.__init__('Jan', 'Kowalski', 44)

d.przedstaw_sie()

# Zwykłą metodę też można wywołać w niestandardowy sposób:
Osoba.przedstaw_sie(d)
