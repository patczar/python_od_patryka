import sqlite3 as sql

import pandas as pd

print('Zaczynamy...')
connection = sql.connect('hr.db')
# emps = pd.read_sql(sql='SELECT * FROM employees ORDER BY employee_id', con=connection)

emps = pd.read_sql(sql='SELECT * FROM employees ORDER BY employee_id',
                   con=connection,
                   index_col='employee_id',
                   parse_dates='hire_date')

print('Mam DataFrame:')
print(emps)

# Gdy dane mamy w postaci DataFrame, możemy przeglądać w taki sposób,
# a do pól w poszczególnych rekordach można odwołać się pisząc
# emp["first_name"] lub emp.first_name
for nr, emp in emps.iterrows():
    print(f'Pracownik {emp.first_name} {emp.last_name} zarabia {emp.salary}')

print()

print('Średnia pensja programistów:', emps[emps.job_id == 'IT_PROG'].salary.mean())

# Wynik zapytania jest wczytywany do pamięci i dostępny w postaci DF.
# Dalsze operacje (filtrowanie, grupowania, agregacja...) odwołują się do danych w pamięci,
# a nie do bazy danych.
# Pandas NIE konwertuje automatycznie swoich wyrażeń na zapytania SQL.
