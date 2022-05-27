# Przykład odczytu z bazy_sql danych PostgreSQL jako przykład połączenia z "prawdziwą bazą danych".
# Wymaga doinstalowania pakietu obsługi bazy PostgreSQL: pip install psycopg2-binary
# Przykład zakłada także działanie serwera PostgreSQL na lokalnym komputerze oraz istnienie przykładowej bazy hr; jest sprawdzony na zasadzie "u mnie działa".
# W porównaniu do SQLite nie działa np. iteracja bezpośrednio po wyniku execute. Można iterować po kursorze lub wczytywać wyniki do pamięci za pomocą fetchall().

# instaluj pakiet psycopg2-binary
import psycopg2
conn = psycopg2.connect("host='localhost' port=5432 dbname='hr' user='hr' password='abc123'")
print(f'Połączenie: {conn}')

c = conn.cursor()
print(f'Kursor: {c}')
print(f'Teraz wykonam zapytanie')
c.execute("SELECT * FROM employees")
print(f'Zapytanie wykonane, teraz wypiszę wyniki iterując po kursorze:')
for row in c:
    print(row)
print()

print(f'Teraz wykonam inne zapytanie wczytując wyniki do pamięci')
c.execute("SELECT country_id, country_name FROM countries ORDER BY country_id")
lista = c.fetchall()
for row in lista:
    print(f'{row[0]} → {row[1]}')

print('Koniec')
