# Zapytaj o kod spółki, początkową i końcową datę
# (format dla dat: YYYYMMDD)
# *dla chętnych: gdy user nie poda daty końcowej, przyjmij datę dzisiejszą

# Gdy już pobierzesz dane:
# - zapisz do pliku csv (nazwa pliku niech zawiera kod oraz daty)
# - podziel dane na miesiące (resample) i np. oblicz średni kurs zamknięcia, ew. dodatkowe pola jak robiliśmy w Jupyterze
# - wygeneruj wykres liniowy i zapisz do pliku
#   → dla chętnych dwie wersje: wykres czterech kursów (otwarcie, zamknięcie, min, max) oraz oddzielnie wstega Belingera

from datetime import date

import pandas as pd

ticker = input('Podaj symbol, np. pkn albo usdpln: ')
pocz =  input('Podaj datę początkową w formacie YYYYMMDD: ')
konc =  input('Podaj datę końcową w formacie YYYYMMDD: ')

# domyślny koniec: dzisiejsza data
if not konc:
    konc = date.today().strftime('%Y%m%d')

# domyślny początek: 1 stycznia z tego samego roku
if not pocz:
    pocz = konc[0:4] + '0101'

adres = f'https://stooq.pl/q/d/l/?s={ticker}&d1={pocz}&d2={konc}&i=d'
df = pd.read_csv(adres, index_col='Data', parse_dates=['Data'])
print(f'Pobrano dane: {len(df)} rekordów')

# nazwy kolumn: Otwarcie 	Najwyzszy 	Najnizszy 	Zamkniecie

print('Najniższy kurs:', df["Najnizszy"].min())
print('Najwyższy kurs:', df["Najwyzszy"].max())
print('Średni kurs zamknięcia:', df["Zamkniecie"].mean())

# Dodamy nowe kolumny
df["Zmiana"] = df["Zamkniecie"].diff()
df["Zmiana %"] = df["Zamkniecie"].pct_change() * 100
df["Średnia 5"] = df["Zamkniecie"].rolling(window=5).mean()

# To poprawiało format daty, ale jednocześnie Excel gubił informację, że ta kolumna jest typu data i stawała się zwykłym tekstem.
# df.index = df.index.strftime('%Y-%m-%d')

# Specyfikacja jak agregować w formie słownika - poniżej przekazuję to do agg
agregaty = {
    'Otwarcie': ['min', 'mean', 'max'],
    'Zamkniecie': ['min', 'mean', 'max'],
    'Najnizszy': ['min'],
    'Najwyzszy': ['max'],
}

# Wolumen agreguję tylko, jesli występuje w danych źródłowych
if 'Wolumen' in df:
    agregaty['Wolumen'] = ['sum']

miesiace = df.resample('M').agg(agregaty)

plik_excel = f'kursy_{ticker}_{pocz}_{konc}.xlsx'
with pd.ExcelWriter(plik_excel) as xl_writer:
    df.to_excel(excel_writer=xl_writer, sheet_name='Dane')
    miesiace.to_excel(excel_writer=xl_writer, sheet_name='Miesiecznie')
print(f'Zapisano plik {plik_excel}')

wykres = df[["Otwarcie", "Zamkniecie", "Najwyzszy", "Najnizszy"]].plot(figsize=(20,10))
plik_wykres = f'kursy_{ticker}_{pocz}_{konc}.png'
wykres.get_figure().savefig(plik_wykres)
print(f'Zapisano wykres w pliku {plik_wykres}')

# Generowanie "wstęgi Boelingera"
WINDOW = 10
KORYTARZ = 2
srednia_kroczaca = df.Zamkniecie.rolling(window=WINDOW).mean()
odchylenie = df.Zamkniecie.rolling(window=WINDOW).std()
wstega_gorna = srednia_kroczaca + KORYTARZ * odchylenie
wstega_dolna = srednia_kroczaca - KORYTARZ * odchylenie

wstega = pd.DataFrame({
    'Bieżące': df['Zamkniecie'],
    'Trend': srednia_kroczaca,
    'Górna': wstega_gorna,
    'Dolna': wstega_dolna,
})

wykres = wstega.plot(figsize=(20, 10), grid=True)
wykres.fill_between(wstega.index, wstega["Górna"], wstega["Dolna"], color="#AAEEFF", alpha=0.25)
plik_bolinger = f'bolinger_{ticker}_{pocz}_{konc}.png'
wykres.get_figure().savefig(plik_bolinger)
print(f'Zapisano wstęgę Bolingera w pliku {plik_bolinger}')
