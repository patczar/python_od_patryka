from random import randrange

lista = [f'+4812300{a}{b}{c}{d}'
         for a in range(1, 6)
         for b in range(10)
         for c in range(10)
         for d in range(10)]

l = len(lista)
print('Długość listy:', l)
print('Wybrane elementy:')
for _ in range(10):
    print(lista[randrange(l)])
