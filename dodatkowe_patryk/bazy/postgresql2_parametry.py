import psycopg2 as sql

connection = sql.connect("host='localhost' port=5432 dbname='hr' user='kurs' password='abc123'")
print(connection)

job = input('Podaj job_id: ')
min_salary = int(input('Podaj minimalną pensję: '))
max_salary = int(input('Podaj maksymalną pensję: '))

c = connection.cursor()
c.execute('SELECT * FROM employees WHERE job_id = %s AND salary BETWEEN %s AND %s', (job, min_salary, max_salary))
for emp in c:
    print(emp)

connection.close()
