import sqlite3 as sql

connection = sql.connect('hr.db')
print('Połączenie otwarte:', connection)

kursor = connection.execute('SELECT * FROM employees')
print(kursor)

# Kursor jest iteratorem, który pozwala przejrzeć wszystkie rekordy wynikowe.
# Każdy rekord jest tuplą.
# Do poszczególnych pól możemy odwoływać się wg numeru pozycji
for rekord in kursor:
    print(rekord)
    print(f' > Pracownik {rekord[1]} {rekord[2]} zarabia {rekord[7]} <')
    print()

# Nie działało:
# print(f'Pracownik {rekord["first_name"]} {rekord["last_name"]} zarabia {rekord["salary"]}')
# print(f'Pracownik {rekord.first_name} {rekord.last_name} zarabia {rekord.salary}')

print("----------------\n")

# Można też od razu wczytać wszystkie wykonowe rekordy do pamięci w formie listy tupli.
zapytanie = '''
SELECT job_title, count(*), avg(salary)
FROM employees JOIN jobs USING(job_id)
GROUP BY job_title
ORDER BY 1
'''


zap2 = 'SELECT job_title, count(*), avg(salary)' \
' FROM employees JOIN jobs USING(job_id)' \
' GROUP BY job_title ' 'ORDER BY 1'


wyniki = connection.execute(zapytanie).fetchall()
print(type(wyniki))
for rekord in wyniki:
    print(f'{rekord[0]:32} | {rekord[1]:2} | {rekord[2]:8.2f}')

connection.close()
