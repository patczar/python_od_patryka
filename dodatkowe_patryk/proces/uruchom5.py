import subprocess

# W tej wersji wyjście jest zapisywane do pliku.
print('Zaczynamy')

with open('output5.txt', mode='w') as plik:
    result = subprocess.run(['find', '..', '-name', '*.py'],
                        stdout=plik, stderr=subprocess.DEVNULL)

print('Gotowe')
