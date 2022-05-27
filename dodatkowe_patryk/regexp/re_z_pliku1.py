import re

# Wersja pokazująca przetwarzanie linia po linii - ale w przypadku tego zadania to nie jest najlepszy sposób.

with open('re_teksty.txt', encoding='utf-8') as wejscie:
    for linia in wejscie:
        # print(linia)
        imie = re.search(r'\w+', linia).group()

        m_kod = re.search(r'\d{2}-\d{3}', linia)
        # w niektórych liniach kodu nie ma
        if m_kod:
            kod = m_kod.group()
        else:
            kod = '-'

        m_email = re.search(r'[\w\-.]+@(\w+\.)+\w+', linia)
        # inny zapis if-a
        email = m_email.group() if m_email else '-'
        print(f'imię: {imie}, kod: {kod}, email: {email}')
