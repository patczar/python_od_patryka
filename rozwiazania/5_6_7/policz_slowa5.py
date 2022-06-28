import re

from zadania2.odmiana import Odmiana

print('Budujemy bazę odmian...')
baza = Odmiana.wczytaj('PoliMorf-0.6.7.tab', lowercase=True)

print('Czytam Pana Tadeusza...')
slownik = {}
licznik = 0
pattern = re.compile(r'\w+')

with open('pan-tadeusz.txt', encoding='utf-8') as plik:
    for linia in plik:
        for slowo in pattern.findall(linia):
            slowo = slowo.lower()
            licznik += 1
            slowo = baza.pierwszaFormaPodstawowa(slowo)
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1

slownik = dict(sorted(slownik.items(), key=lambda para: para[1], reverse=True))

print('Wszystkich słów:', licznik)
for slowo, liczba in slownik.items():
    print(f'{slowo:15} → {liczba:5}')
