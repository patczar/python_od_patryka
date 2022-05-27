# -*- coding: utf-8 -*-

# Pętlę można przerwać wywołując instrukcję break.
# Z kolei continue powoduje pominięcie pozostałych instrukcji w bieżącym obrocie pętli i powrót na początek pętli.

print('Początek programu')

while True:
   liczba = int(input('Podaj liczbę: '))
   if liczba % 7 == 0:
       print('Trafiłeś w liczbę podzielną przez 7. Pętla zostanie zatrzymana.')
       break # skok do linii 18
   if liczba % 5 == 0:
       print('Trafiłeś w liczbę podzielną przez 5. continue wróci na początek pętli.')
       continue # skok do linii 8
   print('Nie było podzielności przez 5 ani 7 - jesteśmy w treści pętli')

print('Koniec programu')

# break i continue są też dostępne dla pętli z warunkiem innym niż True i dla pętli for
