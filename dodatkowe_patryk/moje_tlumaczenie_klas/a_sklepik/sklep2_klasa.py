# W tej wersji stworzymy klasę Sklep.
# Naszym podstawowym celem jest obsługa wielu sklepów jednocześnie.

class Sklep:
    # W tej wersji jeszcze uproszczenie: oba sklepy mają ten sam cennik,
    # gdyby cenniki miały się różnić albo zmieniać w czasie, taki zapis jest niepoprawny.
    # Przy takim zapisie ten sam słownik jest współdzielony przez wszystkie obiekty.
    cennik = {
        'mleko': 3.00,
        'bułka': 1.50,
        'masło': 7.90,
    }

    utarg = 0

    def wypisz_cennik(self):
        print('Nasz asortyment:')
        for t, c in self.cennik.items():
            print(f'{t:10} : {c:6}')
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
            print(f'Za {sztuk} sztuk towaru {towar} zapłacisz {kwota}')
        except KeyError as e:
            print(e)

    def wypisz_utarg(self):
        print(f'Bieżący utarg: {self.utarg}')


# Dzięki temu, że operacje sklepu są zdefiowane w klasie,
# możemy stworzyć kilka obiektów sklep i każdy z nich niezależnie będzie liczył swój utarg.

zabka = Sklep()
biedronka = Sklep()

zabka.wypisz_cennik()
print('Pierwsze zakupy w Żabce:')
zabka.zakupy()

print('\nPierwsze zakupy w Biedronce:')
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
print()

print('Cennik Żabki:')
zabka.wypisz_cennik()

# Zobaczmy, że w tej wersji gdy zmienimy cennik Żabki, to zmieni się również cennik Biedronki. TO JEST TEN SAM OBIEKT (słownik)
zabka.cennik['soczek'] = 3.99
# zabka.cennik = {'soczek': 3.99} - ale to zmienia cennik tylko w Żabce, bo to jest wstawienie nowego obiektu dict

print('Cennik Żabki:')
zabka.wypisz_cennik()

print('Cennik Biedronki:')
biedronka.wypisz_cennik()

