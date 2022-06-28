from odmiana import Odmiana

cs = input('Czy uwzględniać wielkość liter? [T/N] ').upper()
lowercase = cs != 'T'
print('Czytam bazę odmian...')
baza = Odmiana.wczytaj('PoliMorf-0.6.7.tab', lowercase)
print('Baza odmian odmian wczytana')

print('Podawaj słowa do sprawdzenia. Aby zakończyć, wprowadź puste słowo (naciśnij enter).')
while True:
    slowo = input('> ')
    if not slowo: break
    a = baza.znajdzOdmiany(slowo)
    b = baza.znajdzFormyPodstawowe(slowo)
    print(f'Odmiany słowa {slowo}:', *a)
    print(f'Podstawy słowa {slowo}:', *b)

print('Koniec')
