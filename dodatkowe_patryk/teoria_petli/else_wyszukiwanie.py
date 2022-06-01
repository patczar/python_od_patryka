
liczby = [13, 3, 5, 6, 12, 4, 10, 15]

dzielnik = int(input('Podaj dzielnik: '))

# Teraz sprawdzimy czy któraś z tych liczb jest podzielna przez dzielnik
# i jeśli tak, to pierwszy taki element wypiszemy.

for liczba in liczby:
    if liczba % dzielnik == 0:
        print(f'Liczbą podzielną przez {dzielnik} jest {liczba}')
        break
else:
    print(f'Nie znaleziono liczby podzielnej przez {dzielnik}')


print('Ciąg dalszy programu')

# Pętle for oraz while mogą mieć dodatkowo dopisane else:
# Jeśli pętla kończy się z powodu break, to treść else nie jest wykonywana.
# Jeśli pętla kończy się "normalnie" (for doszedł do końca, while ma niespełniony warunek),
# to wtedy else się wykonuje. Również wtedy, gdy program w ogóle nie wszedł do pętli.
# Najczęstsze zastosowanie: jakaś forma wyszukiwania i wykonywania czynności w przypadku niezalezienia.
