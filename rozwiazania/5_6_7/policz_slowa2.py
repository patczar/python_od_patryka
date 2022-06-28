import re

print('Startujemy...')

slownik = {}
licznik = 0

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        slowa = re.findall(r'\w+', linia)
        for slowo in slowa:
            licznik += 1
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1

print('Wszystkich słów:', licznik)
for slowo, liczba in slownik.items():
    print(f'{slowo:15} → {liczba:5}')
