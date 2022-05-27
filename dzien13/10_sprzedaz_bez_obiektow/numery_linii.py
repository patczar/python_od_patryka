
with open('sprzedaz.csv', mode='r', encoding='UTF-8') as plik:
    for nr, linia in enumerate(plik):
        print(f'{nr:6}: {linia}', end='')

