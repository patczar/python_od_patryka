from mathematica import podstawy
from mathematica.algebra import matrices as macierze
from mathematica.geometry import figures

# Sposób importowania pokazany tutaj: from PAKIET import MODUL

wynik = podstawy.pomnoz(2, 3)
print(wynik)

wynik = figures.square_area(5, 3)
print(wynik)
print()


m1 = [[1,1],
      [2,2],
      [3,4]]

m2 = [[0,1],
      [1,0],
      [10,10]]

wynik = macierze.add_matrices(m1, m2)
print(wynik)
print()

import mathematica

print(mathematica.autor)


