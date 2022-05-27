# while WARUNEK: INSTRUKCJE

# Jeśli WARUNEK jest fałszywy, Python nie wykonuje treści pętli i idzie dalej w programie
# Jeśli WARUNEK jest prawdziwy, to Python wykonuje INSTRUKCJE
# i następnie ponownie wraca na początek pętli do sprawdzenia warunku.

# Uwaga, ten przykład jest nienaturalny jak na język Python.
# Do przeglądania kolejnych liczb w Pythonie używa się for x in range...

x = 1
while x <= 5:
    print(x)
    x += 1
print(f'Koniec pętli, teraz x = {x}\n')
print()

from random import randint
suma = 0
while suma < 100:
    los = randint(1, 10)
    suma += los
    print(f'los = {los}, suma = {suma}')
print(f'Gotowe, teraz suma = {suma}')
