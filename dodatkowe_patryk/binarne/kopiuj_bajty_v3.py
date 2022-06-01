# Tutaj argumenty uruchomienia programu podaje się w wierszu poleceń
import sys

# argumentem nr 0 jest nazwa programu
if len(sys.argv) < 3:
    print('Nalezy podac wejscie, wyjscie i opcjonalnie ilosc bajtow')
    exit(1)

BUFSIZE = 4096
WEJSCIE = sys.argv[1]
WYJSCIE = sys.argv[2]
SIZE = None
if len(sys.argv) >= 4:
    SIZE = int(sys.argv[3])

with open(WEJSCIE, mode='rb') as wejscie,\
     open(WYJSCIE, mode='wb') as wyjscie:

    skopiowano = 0
    while not SIZE or skopiowano < SIZE:
        ileczytac = min(SIZE - skopiowano, BUFSIZE) if SIZE else BUFSIZE
        bajty = wejscie.read(ileczytac)
        if not bajty: # koniec pliku przed wczytaniem całego SIZE
            break
        print('porcja rozmiaru', len(bajty))
        skopiowano += len(bajty)
        wyjscie.write(bajty)

print(f'Skopiowano {skopiowano} bajtow')
