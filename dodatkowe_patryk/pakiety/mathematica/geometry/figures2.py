# Opcja 1: z modułu importuję funkcję, podaję ścieżkę bezwzględną
# from mathematica.geometry.measures import cartesian_distanse

# Opcja 2: z pakietu zaimportuj moduł, podaję ścieżkę względną
from .measures import cartesian_distanse

def square_area(a, b):
    return a * b

def triangle_area(a, h):
    return a * h * 0.5

def circle_area(r):
    from math import pi
    return pi * r**2

def square_diagonal(a):
    return cartesian_distanse(a, a)
