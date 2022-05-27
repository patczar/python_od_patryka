#!/usr/bin/python3

# ^ ten dziwny komentarz na górze ma znaczenie w systemach UNIX-owych (np. Linux)
# on wskazuje systemowi operacyjnemu gdzie jest interpreter Pythona
# dzięki temu program można uruchamiać ./przelicznik_walut_2.py zamiast python waluty5.py
# a system traktuje ten plik jak program (taki "exec"), a nie plik tekstowy

import requests

def pobierz_dane(data=None):
    if data: # jeśli data jest podana i jest niepusta
        adres=f'http://api.nbp.pl/api/exchangerates/tables/A/{data}?format=json'
    else: # data nie podana - bierzemy najświeższe dane
        adres=f'http://api.nbp.pl/api/exchangerates/tables/A?format=json'

    dane = requests.get(adres).json()
    return dane[0]


def znajdz_walute(tabela, szukana_waluta):
    for waluta in tabela['rates']:
        if waluta['code'] == szukana_waluta:
            return waluta
    return None


def zajmij_sie_jedna_waluta(waluta):
    kod = waluta['code']
    nazwa = waluta['currency']
    kurs = waluta['mid']
    print(f'Waluta {nazwa} (kod {kod}) ma kurs {kurs}')
    kwota = float(input('Podaj kwotę: '))
    kwotaZlote = kwota * kurs
    print(f'{kwota:.2f} {kod} = {kwotaZlote:.2f} PLN')
    kwotaWaluta = kwota / kurs
    print(f'{kwota:.2f} PLN = {kwotaWaluta:.2f} {kod}')


# Dzięki umieszczeniu treści programu w funkcji main, wszystkie zmienne tworzone w tej funkcji są zmiennymi lokalnymi i inne funkcje nie mają do nich dostępu.
def main():
    try:
        data = input('Podaj datę dla tabeli, lub pusty napis aby pobrać bieżące: ')
        tabela = pobierz_dane(data)
        print('Tabela numer', tabela['no'], 'z dnia', tabela['effectiveDate'])
        while True:
            szukana_waluta = input('Podaj kod waluty (pusty napis aby zakończyć): ').upper()
            if szukana_waluta == '': break
            waluta = znajdz_walute(tabela, szukana_waluta)
            if waluta is None:
                print('Nie ma takiej waluty')
            else:
                zajmij_sie_jedna_waluta(waluta)
    except Exception as e:
        print('Nie udało się pobrać', e)


# Ten if spowoduje, że main (lub cokolwiek pod ifem) wykona się tylko wtedy,
# gdy ten plik jest uruchamiany jako program
# (np. z konsoli: python przelicznik_walut_2.py)

# Ale if będzie nieprawdziwy (i main się nie wykona) jeśli ten plik będzie importowany jako moduł
if __name__ == '__main__':
    main()
