from random import choice

lista = [f'+4812300{i:04}' for i in range(1000, 6000)]

print('Długość listy:', len(lista))
print('Wybrane elementy:')
for _ in range(10):
    print(choice(lista))
