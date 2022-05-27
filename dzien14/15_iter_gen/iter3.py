# Czasami można uprościć uznając, że ten sam obiekt iterowalny jest jednocześnie swoim iteratorem.

class Parzyste:
   def __init__(self, limit = 1000):
       self.liczba = -2
       self.limit = limit

   def __iter__(self):
       return self

   def __next__(self):
       self.liczba += 2
       if self.liczba >= self.limit:
           # gdy chcemy powiadomić Pythona, że iterator już nie da więcej elementów, że to już koniec
           # wtedy wyrzucamy wyjątek StopIteration
           raise StopIteration
       return self.liczba

   def reset(self):
       self.liczba = -2


obiekt = Parzyste()
for i in obiekt:
   print(i)
print()


obiekt = Parzyste(100)
for i in obiekt:
   print(i)
print('----------')
for i in obiekt:
   print(i)

# przy tym podejściu obiekt potrafi przeiterować elementy tylko raz. kolejna pętla na tym samym obiekcie nei wykona się ani razu
# tak działają pliki - po otwarciu linie można odczytać tylko raz (chyba, że potem zrobimy seek(0))

# chyba, że wprowadzimy dodatkową metodę resetującą, która ustawia licznik na 0

print('**********')
obiekt.reset()
for i in obiekt:
   print(i)
