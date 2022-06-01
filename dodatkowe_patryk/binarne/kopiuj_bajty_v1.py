
WEJSCIE = 'plik.txt'
WYJSCIE = 'kopia.txt'
SIZE = 50

with open(WEJSCIE, mode='rb') as wejscie,\
     open(WYJSCIE, mode='wb') as wyjscie:
    bajty = wejscie.read(SIZE)
    print('porcja rozmiaru', len(bajty))
    wyjscie.write(bajty)

print('Gotowe')
