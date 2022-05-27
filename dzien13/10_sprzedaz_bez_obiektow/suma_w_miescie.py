
miasto = 'Katowice'
# oblicz sumę wartości transakcji w tym mieście
suma = 0
with open('sprzedaz.csv', mode='r', encoding='UTF-8') as plik:
    plik.readline()
    for linia in plik:
        t = linia.strip().split(',')
        if t[1] == miasto:
            suma += float(t[5]) * int(t[6])
            # suma = suma + (float(t[5]) * int(t[6]))

print(suma)
print(f'{suma:.2f}')
print('{:.2f}'.format(suma))
print('%.2f' % suma)
