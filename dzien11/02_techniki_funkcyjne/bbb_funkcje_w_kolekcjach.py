# Funkcję można wpisać jako element kolekcji

def powitaj():
    print('Witamy serdecznie')

def pozegnaj():
    print('Do zobaczenia!')


lista_funkcji = [powitaj, pozegnaj, lambda: print('A to jest lambda'), lambda: print('A to kolejna lambda')]
print(lista_funkcji)

for f in lista_funkcji:
    f()



