# rekurencja / rekursja / recursion

def silnia_rek(n):
    if n <= 1: return 1
    return n * silnia_rek(n-1)

# print(silnia_rek(1))
print(silnia_rek(5))

# 5 * (4 * (3 * (2 * (1)))) = 120

def silnia(n):
    wynik = 1
    for i in range(2, n+1):
        wynik *= i
    return wynik

print(silnia(5))


wynik = silnia(1001)
print(wynik)

# rekurencja ma ograniczenie 1000 wywołań - tu będzie RecursionError
# wynik = silnia_rek(1001)
# print(wynik)
