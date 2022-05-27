from konto import Konto

a = Konto(1, 'Ala', 1000)
b = Konto(2, 'Ola', 2000)

print('a:', a)
print('b:', b)

c = b
print('c:', c)
print()

b.wplata(48)
print('a:', a, id(a))
print('b:', b, id(b))
print('c:', c, id(c))
print()

b = a
print('a:', a, id(a))
print('b:', b, id(b))
print('c:', c, id(c))
print()

c = b
print('a:', a, id(a))
print('b:', b, id(b))
print('c:', c, id(c))
print()


