limit = 500

# Rozwiązanie bardziej wydajne #
# Generowane są tylko te kombinacje, które mają sens (a<b<c).
# Okazuje się, że mnożenie jest ZNACZNIE szybsze od potęgowania.
lista = [(a, b, c)
         for c in range(3, limit+1)
         for b in range(2, c)
         for a in range(1, b)
         if a*a + b*b == c*c]

for a, b, c in lista:
    print(f'{a:5}² + {b:5}² = {c:5}²')
print()
print(f'Znaleziono {len(lista)} trójek Pitagorejskich')
