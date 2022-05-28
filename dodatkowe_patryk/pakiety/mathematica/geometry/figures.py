# Opcja 1: z pakietu zaimportuj moduł, podaję ścieżkę bezwzględną
# from mathematica.geometry import measures
# from mathematica.podstawy import pomnoz

# Opcja 2: z pakietu zaimportuj moduł, podaję ścieżkę względną
from . import measures
# from .. import podstawy
from ..podstawy import pomnoz

def square_area(a, b):
    return pomnoz(a, b)

def triangle_area(a, h):
    return a * h * 0.5

def circle_area(r):
    from math import pi
    return pi * r**2

def square_diagonal(a):
    return measures.cartesian_distanse(a, a)
