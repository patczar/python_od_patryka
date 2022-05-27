from konto import Konto

print('Początek pliku')

def f(lista=[], konto=Konto(0, 'Ala')):
    konto.wplata(200)
    lista.append(konto._saldo)
    print(konto, lista)

print('Startujemy')
k1 = Konto(1, 'Ola', 5000)
f([1,2,5], k1)

# gdy uruchamiam z domyślnymi parametrami, to używane są obiekty lista oraz konto podane na początku,
# w linii 3
f()

# i za każdym razem funkcja wywołana bez parametrów, używa tych samych obiektów
f()

k2 = Konto(2, 'Ela', 5000)
f([9,8,7], k2)

f()

print(f)

