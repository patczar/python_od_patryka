
class C:
	def __init__(self, imie, nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko
		self._freezed = True

	def __str__(self):
		return f'Osoba {self.imie} {self.nazwisko}'

	def __setattr__(self, key, value):
		if hasattr(self, '_freezed') and self._freezed:
			raise AttributeError(f'nie wolno już zmieniać obiektu')
		super().__setattr__(key, value)


c = C('Ala', 'Kowalska')
print('Jest obiekt:', c)
try:
	c.imie = 'Alicja'
	print('Udało się ustawić normalnie imię', c.imie)
except Exception as e:
	print('Nie udało się ustawić imienia normalnie')

# da się to objeść wbudowanym słownikiem
try:
	c.__dict__['imie'] = 'Alicja'
	print('Udało się ustawić słownikiem imię', c.imie)
except Exception as e:
	print('Nie udało się ustawić imienia słownikiem')

print(c)