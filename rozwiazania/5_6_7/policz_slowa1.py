import re

print('Startujemy...')

licznik = 0

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        slowa = re.findall(r'\w+', linia)
        for slowo in slowa:
           print('[' + slowo + ']')
           licznik += 1

print('Wszystkich słów:', licznik)
