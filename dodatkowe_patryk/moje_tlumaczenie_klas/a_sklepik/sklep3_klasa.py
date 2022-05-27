# W tej wersji stworzymy klasę Sklep.
# Naszym podstawowym celem jest obsługa wielu sklepów jednocześnie.

class Sklep:
    # W tej wersji każdy obiekt sklep posiada już własny, niezależny cennik.
    # Tak się stanie, gdy cennik wpiszemy do obiektu w metodzie init

    def __init__(self, poczatkowy_cennik):
        self.cennik = poczatkowy_cennik
        self.utarg = 0

    def wypisz_cennik(self):
        print('Nasz asortyment:')
        for t, c in self.cennik.items():
            print(f'{t:12} : {c:8.2f}')
        print()

    def do_zaplaty(self, towar, sztuk=1):
        if towar in self.cennik:
            return self.cennik[towar] * sztuk
        else:
            raise KeyError(f'Nie istnieje produkt o nazwie {towar}')

    def zakupy(self):
        towar = input('Podaj nazwę towaru: ')
        sztuk = int(input(f'Ile sztuk {towar} chcesz kupić? '))
        try:
            kwota = self.do_zaplaty(towar, sztuk)
            self.utarg += kwota
            print(f'Za {sztuk} sztuk towaru {towar} zapłacisz {kwota:8.2f}')
        except KeyError as e:
            print(e)

    def wypisz_utarg(self):
        print(f'Bieżący utarg: {self.utarg:10.2f}')


# Dzięki temu, że operacje sklepu są zdefiowane w klasie,
# możemy stworzyć kilka obiektów sklep i każdy z nich niezależnie będzie liczył swój utarg.

zabka = Sklep({'mleko': 3.00, 'bułka': 1.50, 'masło': 7.90, 'cola': 5.50})

# Teraz Żabka ma swój cennik, ale Lidl i Biedronka będą mieć wspólny.
# Modyfikacja cennika L i B będzie widoczna w obu sklepach na raz.
cennik_lidla_i_biedronki = {'mleko': 2.90, 'bułka': 1.50, 'margaryna': 6.00, 'pepsi': 5.20}
biedronka = Sklep(cennik_lidla_i_biedronki)
lidl = Sklep(cennik_lidla_i_biedronki)

cennik_lidla_i_biedronki['mleko'] += 0.02
# cena mleka w Biedr i Lidl = 2.92

print('Cennik Żabki:')
zabka.wypisz_cennik()
print('Pierwsze zakupy w Żabce:')
zabka.zakupy()

print('\nCennik Biedronki:')
biedronka.wypisz_cennik()
print('Pierwsze zakupy w Biedronce:')
biedronka.zakupy()

print('\nDrugie zakupy w Biedronce:')
biedronka.zakupy()

print('\nTeraz utarg Żabki:', zabka.utarg)
print('Teraz utarg Biedronki:', biedronka.utarg)

print('Drugie zakupy w Żabce:')
zabka.zakupy()

print('\nTeraz utarg Żabki:', zabka.utarg)
print('Teraz utarg Biedronki:', biedronka.utarg)

print('\nSklepy potrafią też same wypisać swój utarg:')
zabka.wypisz_utarg()
biedronka.wypisz_utarg()
