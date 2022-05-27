# Przykład wykonania operacji zmieniających stan.

import sqlite3 as sql
polaczenie = sql.connect('hr.db')

print('Pierwszy INSERT...')
# sql0 = "INSERT INTO countries(country_id, country_name, region_id) VALUES ('PL', 'Poland', 1)"
# polaczenie.execute(sql0)

sql1 = "INSERT INTO countries(country_id, country_name, region_id) VALUES (?, ?, ?)"
polaczenie.execute(sql1, ('PL', 'Poland', 1))

kraje = [
    ('CZ', 'Czechia', 1),
    ('SK', 'Slovakia', 1),
]

print('Seria INSERT-ów...')
sql2 = "INSERT INTO countries(country_id, country_name, region_id) VALUES (?, ?, ?)"
polaczenie.executemany(sql2, kraje)

co_robic = input('Zapisać zmiany? [T/N] ')
if co_robic.strip().upper() == 'T':
    polaczenie.commit()
    print('Zmiany zatwierdzone.')
else:
    polaczenie.rollback()
    print('Zmiany wycofane.')

polaczenie.close()
print('Koniec')
