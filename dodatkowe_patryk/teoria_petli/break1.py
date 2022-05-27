from random import randint

suma = 0
while True:
    los = randint(1, 10)
    suma += los
    if suma >= 100:
        break
    print(f'Po dodaniu {los} suma = {suma}')

print('Już za pętlą, teraz suma = {suma}')
