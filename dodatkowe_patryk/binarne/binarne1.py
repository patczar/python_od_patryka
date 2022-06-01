with open('plik.txt', mode='rb') as plik:
    bajty = plik.read()
print(type(bajty), 'rozmiar:', len(bajty))
print('Pierwszy bajt:', bajty[0]) # wartość liczbowa
print()
for b in bajty:
    print(b, end=', ')
print()
print()
print(bajty)
print()
# zamień na tekst (odkoduj) zgodnie z konkretnym kodowaniem znaków
txt = bajty.decode('UTF-8')
print(txt)

# zgodnie z kodowaniem systemowym
txt = bajty.decode()
print(txt)
