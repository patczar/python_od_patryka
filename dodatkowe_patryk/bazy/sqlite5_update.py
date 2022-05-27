# Program pracownikom z wybranego stanowiska zmienia pensje o podana kwotę

import sqlite3

job = input('Podaj kod stanowiska: ').upper()
podwyzka = int(input('Podaj kwotę podwyżki: '))

c = sqlite3.connect('hr.db')

sql = 'UPDATE employees SET salary = salary + ? WHERE job_id = ?'
c.execute(sql, (podwyzka, job))

co_robic = input('Zapisać zmiany? [T/N] ')
if co_robic.strip().upper() == 'T':
    c.commit()
    print('Zmiany zatwierdzone.')
else:
    c.rollback()
    print('Zmiany wycofane.')

print('Gotowe')
