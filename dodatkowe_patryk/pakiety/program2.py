import modul as m

#ERR wynik = modul.pole_kwadratu(5)

# Przy taki sposobie importowania trzeba używać aliasu przed nazwami funkcji

wynik = m.pole_kwadratu(5)

m.wypisz_tekst(f'Ala ma {wynik} kotów.', 3)

obiekt = m.Klasa()
obiekt.metoda()

print(m.MIASTO)
