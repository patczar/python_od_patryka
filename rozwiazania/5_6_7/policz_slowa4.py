import re

print('Startujemy...')
slownik = {}
licznik = 0
pattern = re.compile(r'\w+')

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        for slowo in pattern.findall(linia):
            licznik += 1
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1

slownik = dict(sorted(slownik.items(), key=lambda para: para[1], reverse=True))

print('Wszystkich słów:', licznik)
for slowo, liczba in slownik.items():
    print(f'{slowo:15} → {liczba:5}')
