from .algebra.matrices import add_matrices

m1 = [[1,1],
      [2,2],
      [3,4]]

m2 = [[0,1],
      [1,0],
      [10,10]]

wynik = add_matrices(m1, m2)
print(wynik)
print()