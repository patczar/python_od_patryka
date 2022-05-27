import re

# Jeśli z wyrażenia korzystamy wielokrotnie (np. w pętli),
# to warto je "skompilować" i korzystać z powstałego obiektu
# To może mocno wpłynąć na wydajność.
imie_pattern = re.compile(r'\w+')
kod_pattern = re.compile(r'\d{2}-\d{3}')
email_pattern = re.compile(r'[\w\-.]+@(\w+\.)+\w+')

with open('re_teksty.txt', encoding='utf-8') as wejscie:
    for linia in wejscie:
        m_imie = imie_pattern.search(linia)
        imie = m_imie.group() if m_imie else '???'

        m_kod = kod_pattern.search(linia)
        kod = m_kod.group() if m_kod else '-'

        m_email = email_pattern.search(linia)
        email = m_email.group() if m_email else '-'

        print(f'imię: {imie}, kod: {kod}, email: {email}')
