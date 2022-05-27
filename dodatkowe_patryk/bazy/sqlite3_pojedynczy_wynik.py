
import sqlite3

polaczenie = sqlite3.connect('hr.db')
ilosc, srednia = polaczenie.execute('SELECT count(*), avg(salary) FROM employees').fetchone()
print('Liczba pracowników:', ilosc)
print('Średnia pensja wszystkich:', srednia)
polaczenie.close()
