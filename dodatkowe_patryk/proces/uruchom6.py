import subprocess

# W tej wersji wejście, wyjście i błedy - wszystko jest w oddzielnych plikach
print('Zaczynamy')

with open('dzialania.txt', mode='r') as wejscie, \
     open('output6.txt', mode='w') as wyjscie, \
     open('bledy6.txt', mode='w') as bledy:
    result = subprocess.run(['python', 'kalkulator.py'],
                        stdin=wejscie, stdout=wyjscie, stderr=bledy)

print('Gotowe. exitcode = ', result.returncode)
