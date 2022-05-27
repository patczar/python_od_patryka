from vector import Vector

def test_str():
    v = Vector(5, 12)
    s = str(v)
    assert s == '<5,12>'


def test_repr():
    v = Vector(5, 12)
    r = repr(v)
    assert r == 'Vector(5,12)'
    new_vector = eval(r)
    assert isinstance(new_vector, Vector)
    assert new_vector.x == 5
    assert new_vector.y == 12


def test_add():
    a = Vector(3, 4)
    b = Vector(5, 12)
    suma = a + b
    assert isinstance(suma, Vector)
    assert suma.x == 8
    assert suma.y == 16


def test_sub():
    a = Vector(3, 4)
    b = Vector(5, 12)
    wynik = b - a
    assert isinstance(wynik, Vector)
    assert wynik.x == 2
    assert wynik.y == 8


def test_mul():
    a = Vector(3, 4)
    wynik = a * 3
    assert isinstance(wynik, Vector)
    assert wynik.x == 9
    assert wynik.y == 12


def test_rmul():
    a = Vector(3, 4)
    wynik = 2 * a
    assert isinstance(wynik, Vector)
    assert wynik.x == 6
    assert wynik.y == 8


def test_eq():
    a = Vector(3, 4)
    b = Vector(4, 3)
    c = Vector(5, 0)
    d = Vector(3, 3)
    assert a == a
    assert a == b
    assert a == c
    assert a != d
