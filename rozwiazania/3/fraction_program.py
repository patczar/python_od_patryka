from fraction import *

def test_gcd_1():
    assert gcd(1, 1) == 1

def test_gcd_rowne():
    assert gcd(17, 17) == 17

def test_gcd_wielokrotnosc():
    assert gcd(77, 11) == 11

def test_gcd_3():
    assert gcd(24, 15) == 3

def test_add_1():
    a = Fraction(2, 3)
    b = Fraction(5, 3)
    res = a + b
    assert res.nominator == 7
    assert res.denominator == 3

def test_add_2():
    a = Fraction(2, 3)
    b = Fraction(3, 5)
    res = a + b
    assert res.nominator == 19
    assert res.denominator == 15

def test_add_3():
    a = Fraction(3, 8)
    b = Fraction(5, 6)
    res = a + b
    assert res.nominator == 29
    assert res.denominator == 24

def test_neg():
    a = Fraction(3, 7)
    res = -a
    assert res.nominator == -3
    assert res.denominator == 7

def test_sub_3():
    a = Fraction(3, 8)
    b = Fraction(5, 6)
    res = b - a
    assert res.nominator == 11
    assert res.denominator == 24

def test_mul_1():
    a = Fraction(2, 3)
    b = Fraction(11, 7)
    res = a * b
    assert res.nominator == 22
    assert res.denominator == 21

def test_mul_2():
    a = Fraction(2, 3)
    b = Fraction(6, 7)
    res = a * b
    assert res.nominator == 4
    assert res.denominator == 7

def test_div_1():
    a = Fraction(3412, 101)
    b = Fraction(3412, 101)
    res = a / b
    assert res.nominator == 1
    assert res.denominator == 1

def test_div_2():
    a = Fraction(2, 3)
    b = Fraction(7, 6)
    res = a / b
    assert res.nominator == 4
    assert res.denominator == 7

def test_int():
    a = Fraction(7, 4)
    assert int(a) == 1

def test_float():
    a = Fraction(7, 4)
    assert float(a) == 1.75

def test_true():
    a = Fraction(7, 4)
    assert bool(a) == True

def test_false():
    a = Fraction(0, 4)
    assert bool(a) == False
