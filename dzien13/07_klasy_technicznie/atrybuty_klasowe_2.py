class Klasa:
   # W Pythonie, podobnie jak w C++ czy Javie, można deklarować atrybuty w ciele klasy (a nie w init).
   # Jednak w Pythonie działa to w sposób specyficzny, nieoczywisty.
   # Te zmienne są przechowywane w klasie, a nie w obiekcie, a obiekty mają do nich dostęp.
   # Jednak zapisanie atrybutu o tej samej nazwie w obiekcie (poprzez self) przesłania definicję z poziomu klasy.

   x = 100
   s = 'Ala ma kota'
   lista = []

   def __init__(self, y):
       self.y = y

   def __str__(self):
       return f'x = {self.x} , y = {self.y}, s = {self.s}, lista: {self.lista}'

   def dodajZwierze(self, zwierze):
       self.s += f' oraz {zwierze}'


a = Klasa(1)
print('a:', a)

b = Klasa(2)
print('b:', b)
print()

print("x z różnych perspektyw:")
print(a.x)
print(b.x)
print(Klasa.x)
print()

# Tutaj operacja jest wykonywana na zmiennej klasy
# Obiekty - jeśli nie "przesłoniły" tej zmiennej, to widzą tę zmianę.
# x jest atrybutem klasowym, do którego dostęp jest możliwy także poprzez obiekty
Klasa.x += 3
print(a.x)
print(b.x)
print(Klasa.x)
print('a.__dict__:', a.__dict__)
print('Klasa.__dict__:', Klasa.__dict__)
print()

# Teraz obiekt a tworzy własny atrybut, który przesłoni dostep do x klasowego
# a.x += 5     jest traktowane jako a.x = a.x + 5      w tym przypadku   a.x = Klasa.x + 5
a.x += 5
print(a.x)
print(b.x)
print(Klasa.x)
# od tej pory a ma swojego własnego x
# natomiast b.x oznacza odwołanie do Klasa.x
print('a.__dict__:', a.__dict__)
print('Klasa.__dict__:', Klasa.__dict__)
print()

Klasa.x += 1
print(a.x)
print(b.x)
print(Klasa.x)
print()

print(a.lista)
print(b.lista)

# operacja modyfikująca listę modyfikuje listę przechowywaną w klasie , zmiany będą widoczne dla wszystkich obiektów klasy
a.lista.append('Ala')
b.lista.append('Ola')
Klasa.lista.append('Ela')

print(a.lista)
print(b.lista)
print(Klasa.lista)
print()

print(a)
print(b)
print()

Klasa.s = 'Ola ma psa'
# a i b widzą tę zmianę
print(a)
print(b)

b.dodajZwierze('rybki')
# od teraz b używa swojej kopii napisu s
print(a)
print(b)

Klasa.s = 'Ela ma królika'
# Tylko a widzi zmianę, b już nie, bo używa swojej kopii napisu
print(a)
print(b)

