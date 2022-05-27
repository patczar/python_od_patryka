# Przykład wykonania operacji zmieniających stan.

import psycopg2
conn = psycopg2.connect("host='localhost' dbname='hr' user='kurs' password='abc123'")
c = conn.cursor()

print('Pierwszy INSERT...')
sql1 = "INSERT INTO countries(country_id, country_name, region_id) VALUES ('PL', 'Poland', 1)"
c.execute(sql1)

kraje = [
    ('CZ', 'Czechia', 1),
    ('SK', 'Slovakia', 1),
]

print('Seria INSERT-ów...')
sql2 = "INSERT INTO countries(country_id, country_name, region_id) VALUES (%s, %s, %s)"
c.executemany(sql2, kraje)

co_robic = input('Zapisać zmiany? [T/N] ')
if co_robic.strip().upper() == 'T':
    conn.commit()
    print('Zmiany zatwierdzone.')
else:
    conn.rollback()
    print('Zmiany wycofane.')

conn.close()
print('Koniec')
