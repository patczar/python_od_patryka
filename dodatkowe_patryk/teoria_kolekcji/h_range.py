# range to generator, który generuje kolejne liczby z podanego zakresu
# range ma możliwości zbliżone do "wycinanek listowych" (slices):

# Najbardziej ogólna postać:
# range(start, stop, step)
# Liczba od której zaczynamy, PRZED którą kończymy, o ile idziemy w każdym kroku

# Najczęściej używa się range w połączeniu z pętlą for, aby wykonać operację dla kolejnych liczb.
for a in range(10, 30, 3):
    print("a = ", a)
print()

for b in range(20, 40, 2):
    print(b, end=', ')
print()

# Możliwości...
# Domyślnym krokiem jest 1
# range(start, stop)

for b in range(20, 40):
    print(b, end=', ')
print()

# Domyślnym początkiem jest 0
# range(stop)
for b in range(10):
    print(b, end=', ')
print()

# Krok może być ujemny
for b in range(50, 40, -1):
    print(b, end=', ')
print()

# Samo odwrócenie wartości start/stop nie wystarcza, bo domyślny krok to jest +1
# Tu nic się nie wypisze:
for b in range(90, 80):
    print(b, end=', ')
print()

print("\n==============\n")

# Stara wersja notatek

# gdy podajemy jeden argument n, to generowane są liczby od 0 do n-1
for i in range(10):
	print(i)
print("==============")

# gdy podajemy dwa argumenty poczatek , koniec,
# to generowane są liczby od poczatek wlacznie, do koniec wylaczajac
for i in range(5, 10):
	print(i)
print("==============")

# trzeci parametr oznacza wielkość kroku, może być ujemny
for i in range(10, 20, 3):
	print(i)
print("==============")

# gdy krok jest ujemny, to sprawdzane jest czy i > koniec
for i in range(10, 0, -1):
	print(i)
print("==============")

# range jest "generatorem", to znaczy nie zawiera w sobie tych wszystkich liczb na raz, tylko potrafi je wygenerować
# można bez problemu stworzyć zmienną z zakresem, któryc nie zmieściłby się w pamięci
mega_zakres = range(0, 1000_000_000_000)
print(mega_zakres)

# gdybym próbował utworzyć taką listę, to pamięci zabraknie
# MemoryError
mega_lista = list(mega_zakres)
print(len(mega_lista))

# Ale liczby są dostępne, gdy przetwarzamy je np. w pętli for
# for i in mega_zakres:
#     print(i)
#     if i > 1000000: break  # żeby jednak się zakończył

