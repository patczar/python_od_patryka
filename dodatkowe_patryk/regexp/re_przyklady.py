import re

txt1 = 'Ala ma kota, Ola ma psa, Zuzia ma rybki, Ela ma świnkę, babulaxyz.'

txt2 = '''
Ala ma kota Filemona.
Ola ma psa Burka.
Linia, która nie pasuje.
Bożena ma rybkę.
p12_inne bzdury
'''

mail = 'ala.kowalska@gmail.com'
zlymail = 'ala$toniejestmail.pl'
mail_z_dodatkami = 'ala.kowalska@gmail.com i jeszcze jakieś bzdury'
mail_w_ukryty_w_srodku = 'początkowe bzdury ala.kowalska@gmail.com i jeszcze jakieś bzdury'

# match : dopasowuje początek tekstu do wzorca
print('match')

wzorzec_emaila = r'[A-Za-z0-9_.\-]+@([A-Za-z0-9_\-]+\.)+[A-Za-z]+'

# Jeśli napis uda się dopasować do wzorca, to wynikiem jest obiekt Match opisujący szczegóły dopasowania
# m = re.match('.+@.+', mail)
m = re.match(wzorzec_emaila, mail)
print('wynik dla dobrego maila:', m)

# match kończy się sukcesem, gdy tekst na początku zawiera szukany fragment

# Jeśli napisu nie uda się dopasować, to wynikiem jest None
m = re.match(wzorzec_emaila, zlymail)
print('wynik dla złego maila:', m)

m = re.match(wzorzec_emaila, mail_z_dodatkami)
print('wynik dla maila z dodatkami:', m)

m = re.match(wzorzec_emaila, mail_w_ukryty_w_srodku)
print('wynik dla maila ukrytego w środku:', m)

# Najbardziej typowy zapis wykorzystujący match:
m = re.match(wzorzec_emaila, mail_z_dodatkami)
if m:
    print('Tekst pasuje')
    print('Pozycje znalezionego tekstu:', m.start(), m.end())
    print('Dopasowany fragment:', m.group())  # albo m[0]
    print('Wycięty fragment:', mail_z_dodatkami[m.start():m.end()])
else:
    print('Tekst nie pasuje')
print('\n----------\n')

m = re.match(r'.la', txt1)
print('match:', m)

m = re.fullmatch(r'.la', txt1)
print('fullmatch:', m)
print()

# fullmatch : dopasowuje cały tekst do wzorca
# Zwraca None jeśli tekst zawiera dodatkowe znaki na końcu
print('fullmatch')

m = re.fullmatch(wzorzec_emaila, mail)
print('wynik dla dobrego maila:', m)

# Jeśli napisu nie uda się dopasować, to wynikiem jest None
m = re.fullmatch(wzorzec_emaila, zlymail)
print('wynik dla złego maila:', m)

m = re.fullmatch(wzorzec_emaila, mail_z_dodatkami)
print('wynik dla maila z dodatkami:', m)

m = re.fullmatch(wzorzec_emaila, mail_w_ukryty_w_srodku)
print('wynik dla maila ukrytego w środku:', m)

print('\n----------\n')

# search - szuka wystąpienia wzorca wewnątrz tekstu, nie musi on być na początku
# znajduje pierwsze (ale maksymalne) dopasowanie
print('search')

m = re.search(r'.la', txt1)
print(m)

m = re.search(r'.la', txt1)
print(m) # zwraca to sam, nie idzie dalej

# w praktyce możemy wyciąć fragment napisu
m = re.search(r'.la', txt1[10:])
print(m) # zwraca to sam, nie idzie dalej


m = re.search(r'k..a', txt1)
print(m)

m = re.search('chomik', txt1)
print(m)

# . oznacza dowolny
# \. oznacza kropkę
m = re.search(r'..\.', txt1)
print(m)

print()

m = re.search(wzorzec_emaila, mail)
print('wynik dla dobrego maila:', m)

# Jeśli napisu nie uda się dopasować, to wynikiem jest None
m = re.search(wzorzec_emaila, zlymail)
print('wynik dla złego maila:', m)

m = re.search(wzorzec_emaila, mail_z_dodatkami)
print('wynik dla maila z dodatkami:', m)

m = re.search(wzorzec_emaila, mail_w_ukryty_w_srodku)
print('wynik dla maila ukrytego w środku:', m)

print('\n----------\n')

# findall : zwraca listę wszystkich dopasowanych fragmentów (listę stringów)

lista = re.findall(r'.la', txt1)
print(lista)

lista = re.findall(r'\w+ ma \w+', txt2)
print(lista)
print('\n----------\n')

# finditer - zwraca iterator pozwalający odczytać szczegóły kolejnych dopasowań
# x = re.finditer(r'.la', txt1)
# print(x)

for m in re.finditer(r'.la', txt1):
    print('Znaleziono', m)
print()

for m in re.finditer(r'\w+ ma \w+', txt2):
    print(f'Znaleziono napis "{m.group()}" na pozycji od {m.start()} do {m.end()}')

print('\n----------\n')

# Za pomocą nawiasów okrągłych mogę oznaczać fragmenty wzorców - potem traktować jako tzw. grupy

for m in re.finditer(r'(\w+) ma (\w+)', txt2):
    print('Cały napis:', m.group())
    print('  Grupa 0:', m.group(0))
    print('  Osoba:', m.group(1))
    print('  Zwierzę:', m.group(2))
    # zamiast wywoływać group można też użyć indeksacji
    print('  Osoba:', m[1])
    print('  Zwierzę:', m[2])
    #cale, osoba, zwierze = m
    #print(cale, osoba, zwierze)

    print()
print('\n----------\n')

# Jeśli mam taką potrzebę, to mogę wziąć pewien fragment w nawias, ale nie robić z niego grupy - zapis (?:  tzw. "grupa anonimowa"
print('Grupy anonimowe:')
for m in re.finditer(r'(?:\w+) ma (\w+)', txt2):
    print('Cały napis:', m.group())
    print('  grupa 1:', m.group(1))
    print()
print('\n----------\n')

# Jeśli szukamy po jednym fragmencie w każdej linii, to lepiej zastosować schemat
# for linia in linie: match

linie = txt2.split('\n')
for linia in linie:
    #print(linia)
    m = re.match(r'(\w+) ma (\w+)', linia)
    if m:
        print(f'Zalezione: imie = {m[1]}, zwierze = {m[2]}')
    else:
        print('  -- nie pasuje --')
print()

print('========')
# w celu zwiększenia wydajności regexpa używane wielokrotnie (np. w pętli) warto wcześniej skompilować
pattern = re.compile(r'(\w+) ma (\w+)')
for linia in linie:
    #print(linia)
    m = pattern.match(linia)
    if m:
        print(f'Zalezione: imie = {m[1]}, zwierze = {m[2]}')
    else:
        print('  -- nie pasuje --')


