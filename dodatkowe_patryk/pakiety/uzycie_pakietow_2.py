from mathematica.algebra.matrices import *
from mathematica.podstawy import pomnoz

# Sposób importowania pokazany tutaj: from PAKIET.MODUL import FUNKCJA

wynik = pomnoz(2, 3)
print(wynik)

m1 = [[1,1],
      [2,2],
      [3,4]]

m2 = [[0,1],
      [1,0],
      [10,10]]

wynik = add_matrices(m1, m2)
print(wynik)
print()

from mathematica import autor
print(autor)

