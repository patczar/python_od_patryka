print('Początek programu, teraz __name__ == ', __name__)
print('Zaraz będzie import...')

import modul

# Przy taki sposobie importowania trzeba używać nazwy modułu przed nazwami funkcji

wynik = modul.pole_kwadratu(5)

modul.wypisz_tekst(f'Ala ma {wynik} kotów.', 3)

obiekt = modul.Klasa()
obiekt.metoda()

print(modul.MIASTO)

print('Próba drugiego importu')
# Moduł jest importowany tylko jeden raz. Kolejny import już nic nie robi.

print('Koniec programu')
