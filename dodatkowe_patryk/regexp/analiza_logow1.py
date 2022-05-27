import re

pattern = re.compile(r'^([^\|]+)\|install\|([^\|]+)\|([^\|]+)\|')

with open('zypper.log') as plik:
    for linia in plik:
        m = pattern.match(linia)
        if m:
            data = m[1]
            pakiet = m[2]
            wersja = m[3]
            if 'python' in pakiet:
                print('Pakiet', pakiet, 'w wersji', wersja, 'zainstalowano w dniu', data)

