import re

# Wersja pokazująca przetwarzanie linia po linii - ale w przypadku tego zadania to nie jest najlepszy sposób.

with open('re_teksty.txt', encoding='utf-8') as wejscie:
    for linia in wejscie:
        m_imie = re.search(r'\w+', linia)
        imie = m_imie.group() if m_imie else '???'

        m_kod = re.search(r'\d{2}-\d{3}', linia)
        kod = m_kod.group() if m_kod else '-'

        m_email = re.search(r'[\w\-.]+@(\w+\.)+\w+', linia)
        email = m_email.group() if m_email else '-'

        print(f'imię: {imie}, kod: {kod}, email: {email}')
