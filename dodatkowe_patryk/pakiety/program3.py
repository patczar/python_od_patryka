from modul import wypisz_tekst, Klasa, MIASTO

# Przy takim sposobie importowania w kodzie używamy samych nazw funkcji
# a nie nie możemy już uzywać nazwy moduły (i dostawać się do innych funkcji)

# wynik = modul.pole_kwadratu(5)
# modul.wypisz_tekst(f'Ala i jej kot', 3)

wypisz_tekst(f'Ala mieszka w {MIASTO}', 3)

obiekt = Klasa()
obiekt.metoda()

print(MIASTO)
