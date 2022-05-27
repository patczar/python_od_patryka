# W tej wersji funkcja, którą chcemy przetestować, oraz jej testy umieszczamy w jednym pliku.
# 0 1 1 2 3 5 8 13 21 34 55

import pytest

def fib(n):
    if n < 0:
        raise ValueError('Ujemny argument fib')
    biezaca = 0
    poprzednia = 1
    for i in range(n):
        biezaca, poprzednia = biezaca + poprzednia, biezaca
    return biezaca

@pytest.mark.parametrize("argument,wynik",
                         [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55), (100, 354224848179261915075)])
# @pytest.mark.timeout(10)
def test_fib(argument, wynik):
    assert fib(argument) == wynik

def test_fib_ujemna():
    # ma dojść do takiego wyjątku
    with pytest.raises(ValueError):
        fib(-1)
