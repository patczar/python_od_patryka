# Używamy dwóch modułów ze standardowej biblioteki Pythona
import json
from urllib import request

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

print('Pobieram dane...')

# Bez żadnych dodatkowych bibliotek można pobrać dane z sieci i potraktować jak JSON-a w taki sposób:
with request.urlopen(ADRES) as response:
    txt = response.read().decode('utf-8')

# print('Pobrane dane:', txt)

dane = json.loads(txt)
# print(type(dane))

tabela = dane[0]

print(f'Tabela nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')

for rate in tabela["rates"]:
    print(f'{rate["code"]:3} : {rate["mid"]:<10} - {rate["currency"]}')

