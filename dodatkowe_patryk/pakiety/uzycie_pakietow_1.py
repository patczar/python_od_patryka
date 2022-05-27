import mathematica.algebra.matrices
import mathematica.podstawy

# Sposób importowania pokazany tutaj: import PAKIET.MODUL
# Konsekwencja: podczas wywoływania funkcji lub klas trzeba wpisywać pełną ścieżkę

wynik = mathematica.podstawy.pomnoz(2, 3)
print(wynik)

m1 = [[1,1],
      [2,2],
      [3,4]]

m2 = [[0,1],
      [1,0],
      [10,10]]

wynik = mathematica.algebra.matrices.add_matrices(m1, m2)
print(wynik)

import mathematica

print(mathematica.autor)
print(mathematica.domyslna_funkcja(7, 5))
