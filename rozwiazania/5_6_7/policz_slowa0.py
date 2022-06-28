print('Startujemy...')

licznik = 0

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        slowa = linia.strip().split()
        for slowo in slowa:
           print('[' + slowo + ']')
           licznik += 1

print('Wszystkich słów:', licznik)
