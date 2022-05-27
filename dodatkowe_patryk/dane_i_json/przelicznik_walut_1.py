# Napisz program, który pozwala przeliczać kwotę z PLN na inną walutę i vice versa

# Kolejne wersje/funkcjonalności:
# - przeliczanie jednej waluty zgodne z dzisiejszym kursem
# - program raz pobiera kursy, a później działa w pętli i wielokrotnie prosi o podanie waluty i kwoty
# - przy uruchomieniu programu można podać datę i wtedy wczytywane są kursy archiwalne z podanej daty
#   a następnie można wypisać kurs lub przeliczyć kwotę dla wybranej waluty

import requests

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
try:
    print('Pobieram dane...')
    dane = requests.get(ADRES).json()
    tabela = dane[0]
    print('Tabela numer', tabela["no"], 'z dnia', tabela["effectiveDate"])
    waluty = tabela["rates"]

    szukana_waluta = input('Podaj kod waluty: ').upper()
    kwota = float(input('Podaj kwotę: '))

    for waluta in waluty:
        if waluta["code"] == szukana_waluta:
            kod = waluta["code"]
            nazwa = waluta["currency"]
            kurs = waluta["mid"]

            print(f'Waluta {nazwa} (kod {kod}) ma kurs {kurs}')
            kwotaZlote = kwota * kurs
            print(f'{kwota:.2f} {kod} = {kwotaZlote:.2f} PLN')
            kwotaWaluta = kwota / kurs
            print(f'{kwota:.2f} PLN = {kwotaWaluta:.2f} {kod}')
            break
    else:
        print(f'Nie ma takiej waluty {szukana_waluta}')

except Exception as e:
    print('Nie udało się pobrać', e)

