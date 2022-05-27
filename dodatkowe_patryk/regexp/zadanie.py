# Napisz program znajdujący w dostarczonym pliku wszystkie wystąpienia:
# I kodów pocztowych - 12-123
# I adresów email - test@email.com
# I dat - 12 Jan 1990
# Skorzystaj z modułu re.

import re

with open('re_teksty.txt') as plik:
    tresc = plik.read()

kody = re.findall(r'\d{2}-\d{3}', tresc)
print('Kody pocztowe:', kody)

# daty = re.findall(r'\d{1,2} \w{3} \d{4}', tresc)
daty = re.findall(r'\d{1,2} [A-Z][a-z]{2} \d{4}', tresc)
print('Daty:', daty)

maile = re.findall(r'[\w\-.]+@(?:\w+\.)+[a-z]+', tresc)
print('Emaile:', maile)
