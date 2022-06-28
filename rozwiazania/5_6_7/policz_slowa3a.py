import re

print('Startujemy...')

slownik = {}
licznik = 0

pattern = re.compile(r'\w+')

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        for match in pattern.finditer(linia):
            slowo = match.group(0)
            licznik += 1
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1

print('Wszystkich słów:', licznik)
for slowo, liczba in slownik.items():
    print(f'{slowo:15} → {liczba:5}')
