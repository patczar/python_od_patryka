
WEJSCIE = '/dev/random'
WYJSCIE = 'random.dat'
BUFSIZE = 1024
SIZE = 5000

with open(WEJSCIE, mode='rb') as wejscie,\
     open(WYJSCIE, mode='wb') as wyjscie:

    pozostalo = SIZE
    while pozostalo > 0:
        bajty = wejscie.read(min(pozostalo, BUFSIZE))
        if not bajty: # koniec pliku przed wczytaniem całego SIZE
            break
        print('porcja rozmiaru', len(bajty))
        pozostalo -= len(bajty)
        wyjscie.write(bajty)

print('Gotowe')
