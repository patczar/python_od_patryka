# break jest szczególnie użyteczny, gdy w pętli musimy wykonać pierwszy krok
# (np. wczytać dane) i dopiero wtedy wiemy czy pętlę przerwać, czy kontynuować

suma = 0

while True:
    liczba = int(input('Podaj kolejną liczbę, 0 aby zakończyć: '))
    if liczba == 0:
        break
    suma += liczba
    print(f'Po dodaniu {liczba} suma jest równa {suma}')

print('KONIEC')
