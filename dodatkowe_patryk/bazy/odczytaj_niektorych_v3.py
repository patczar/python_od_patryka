import sqlite3 as sql

connection = sql.connect('hr.db')
print('Połączenie otwarte:', connection)

kod = input('Podaj kod stanowiska, np. IT_PROG : ')
# TODO Odczytaj z tabeli tylko tych pracowników, którzy mają takie job_id

c = connection.execute(f"SELECT * FROM employees WHERE job_id = ?", (kod,))
for emp in c:
    print(emp)

connection.close()
