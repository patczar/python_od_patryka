import re

szukane = input('Podaj szukane słowo: ')

pattern = re.compile(r'\w+')
licznik = 0
with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        slowa = pattern.findall(linia.strip())
        for slowo in slowa:
           if slowo == szukane:
            licznik += 1

print('Słowo', szukane, 'występuje', licznik, 'razy.')
