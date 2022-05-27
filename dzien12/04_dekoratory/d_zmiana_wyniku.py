
def neg(f):
    def wrapper(*args, **kwargs):
        wynik = f(*args, **kwargs)
        return -wynik
    return wrapper

@neg
def silnia(n):
    iloczyn = 1
    for i in range(2, n+1):
        iloczyn *= i
    return iloczyn

print(silnia(5))
print(silnia(10))




