# Z pakietu mathematica.algebra (ścieżka bezwzględna) import modułu matrices
# tak jakby /mathematica/algebra/matrices.py

from mathematica.algebra import matrices

def test_add_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    b = [
        [7, 8, 9],
        [10, 11, 12],
    ]

    result = matrices.add_matrices(a, b)

    assert result == [
        [8, 10, 12],
        [14, 16, 18],
    ]


def test_sub_matrices():
    a = [
        [12, 11, 10],
        [9, 8, 7],
    ]
    b = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    result = matrices.sub_matrices(a, b)

    assert result == [
        [11, 9, 7],
        [5, 3, 1],
    ]
