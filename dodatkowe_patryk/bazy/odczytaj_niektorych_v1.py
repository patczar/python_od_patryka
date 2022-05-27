import sqlite3 as sql

connection = sql.connect('hr.db')
print('Połączenie otwarte:', connection)

kod = input('Podaj kod stanowiska, np. IT_PROG : ')
# TODO Odczytaj z tabeli tylko tych pracowników, którzy mają takie job_id

# Rozwiązanie mało wydajne:
# Baza odczytuje wszystkie rekordy, nie korzysta w żaden sposób z indeksów itp. rozwiązań,
# w przypadku "prawdziwej" bazy danych - wszystkie dane są transferowane przez sieć
# i aplikacja kliencka wszystkie dane przegląda w pętli.

c = connection.execute('SELECT * FROM employees')
for emp in c:
    if emp[6] == kod:
        print(emp)

connection.close()
