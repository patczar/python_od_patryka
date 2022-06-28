limit = 500

# Rozwiązanie mało wydajne.
# Potęgowanie, nawet **2, działa wolniej od mnożenia.
# W dodatku tutaj generujemy wszystkie możliwe kombinacje liczb i dopiero potem sprawdzamy warunkiem.
lista = [(a, b, c)
         for a in range(1, limit+1)
         for b in range(1, limit+1)
         for c in range(1, limit+1)
         if a < b < c and a**2 + b**2 == c**2]

for a, b, c in lista:
    print(a, b, c)
print()
print(f'Znaleziono {len(lista)} trójek Pitagorejskich')
