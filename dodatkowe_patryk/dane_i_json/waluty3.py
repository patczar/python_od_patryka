import requests

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

print('Pobieram dane...')
dane = requests.get(ADRES).json()

tabela = dane[0]
print(f'Tabela nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')

for rate in tabela["rates"]:
    print(f'{rate["code"]:3} : {rate["mid"]:<10} - {rate["currency"]}')

