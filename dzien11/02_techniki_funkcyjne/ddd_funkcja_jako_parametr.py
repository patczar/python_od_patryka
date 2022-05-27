# Funkcja wykonuje przekazaną funkcję f tyle razy, ile wynosi ileRazy

def powtorz(f, ileRazy, *args, **kwargs):
    for i in range(ileRazy):
        f(*args, **kwargs)

def powitaj():
    print('Witamy serdecznie')


powtorz(powitaj, 3)
print()

# następny krok: dodaj do funkcji powtórz takie elementy, aby można byo uruchamiać również funkcje z argumentami
powtorz(print, 5, 'Ala ma kota')
print()
powtorz(print, 5, 'Ala', 'Ela', 'Ola', sep=';')

