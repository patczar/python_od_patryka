import re

# wersja Konrada

POST_CODE_PATTERN = re.compile(r'\d{2}-\d{3}')
EMAIL_PATTERN = re.compile(r'[\w\-]+@(?:\w+\.)+\w+')
DATE_PATTERN = re.compile(r'\d{1,2} \w{3} \d{4}')

with open('re_teksty.txt', encoding='utf-8') as f:
    tresc = f.read()
    print('Kody pocztowe:', ', '.join(POST_CODE_PATTERN.findall(tresc)))
    print('Adresy email:', ', '.join(EMAIL_PATTERN.findall(tresc)))
    print('Daty:', ', '.join(DATE_PATTERN.findall(tresc)))
