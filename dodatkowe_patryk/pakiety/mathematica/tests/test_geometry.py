# Można importować podając ścieżkę bezwzględną
# from mathematica.geometry import figures

# Ale jeśli jesteśmy w tym pakiecie (mathematica.test),
# to możemy importować podając ścieżkę względną
# To odpowiada ścieżce do plików:    ../geometry/figures.py
# Trzeba wejść poziom wyżej, bo jesteśmy w pakiecie tests
from ..geometry import figures


def test_square_area():
    assert figures.square_area(a=2, b=3) == 6


def test_triangle_area():
    assert figures.triangle_area(a=2, h=4) == 4
