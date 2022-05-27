import re

with open('re_teksty.txt', encoding='utf-8') as f:
    tresc = f.read() # wczytaj cały plik jako jeden string

kody = re.findall(r'\d{2}-\d{3}', tresc)
print('Kody pocztowe: ', kody)

emaile = re.findall(r'[\w\-]+@(?:\w+\.)+\w+', tresc)
print('Adresy email: ', emaile)

daty = re.findall(r'\d{1,2} \w{3} \d{4}', tresc)
print('Daty: ', daty)
