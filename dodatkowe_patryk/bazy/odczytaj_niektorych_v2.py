import sqlite3 as sql

connection = sql.connect('hr.db')
print('Połączenie otwarte:', connection)

kod = input('Podaj kod stanowiska, np. IT_PROG : ')
# TODO Odczytaj z tabeli tylko tych pracowników, którzy mają takie job_id

# W tej wersji już baza danych dokonuje filtrowania i może skorzystać z indeksów.
# Jednak doklejanie danych wprowadzonych przez użytkownika do treści zapytanie SQL jest NIEBEZPIECZNE.
# "SQL injection". Tutaj można zmodyfikować warunek logiczny,
# np. a' OR 'a' = 'a
# spowoduje wyświetlenie wszystkich rekordów
# a a' or job_id = (MEGASKOMPLIKOWANE PODZAPYTANIE) or 'a' = 'a
# "zawiesza" bazę danych

c = connection.execute(f"SELECT * FROM employees WHERE job_id = '{kod}'")
for emp in c:
    print(emp)

connection.close()
