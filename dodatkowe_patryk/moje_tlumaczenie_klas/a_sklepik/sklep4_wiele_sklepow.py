class Sklep:
    def __init__(self, nazwa, poczatkowy_cennik={}):
        self.nazwa = nazwa
        # Dzięki zapisowi dict(parametr) w nowotworzonym obiekcie umieścimy kopię słownika przekazanego w parametrze
        self.cennik = dict(poczatkowy_cennik)
        self.utarg = 0

    def wypisz_cennik(self):
        print(f'Asortyment sklepu {self.nazwa}:')
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

    def zmien_cennik(self):
        towar = input('Podaj nazwę towaru: ')
        cena = float(input('Podaj nową cenę: '))
        self.cennik[towar] = cena

    def usun_towar(self):
        towar = input('Podaj nazwę towaru, który chcesz usunąć: ')
        if towar in self.cennik:
            del self.cennik[towar]
        else:
            print(f'Nie ma towaru o nazwie {towar}')

    def wypisz_utarg(self):
        print(f'Bieżący utarg sklepu {self.nazwa}: {self.utarg:10.2f}')


def wybierz_sklep(sklepy):
    print('Dostępne sklepy:', sklepy.keys())
    nazwa_sklepu = input('Podaj nazwę sklepu: ')
    return sklepy[nazwa_sklepu]


def main():
    # w tym słowniku dla nazwy sklepu pamiętamy obiekt sklep
    sklepy = {}

    while True:
        print('\nWybierz operacje:')
        print(' Q - zakończ program')
        print(' N - utwórz nowy sklep')
        print(' P - wypisz cennik')
        print(' K - zakupy')
        print(' C - wprowadź cenę towaru')
        print(' D - usuń towar z cennika')
        print(' U - wypisz utarg sklepu')

        wybor = input(": ").strip().upper()
        if wybor == 'Q':
            break
        elif wybor == 'N':
            nazwa_sklepu = input('Podaj nazwę sklepu: ')
            sklep = Sklep(nazwa_sklepu)
            sklepy[nazwa_sklepu] = sklep
        elif wybor == 'P':
            sklep = wybierz_sklep(sklepy)
            sklep.wypisz_cennik()
        elif wybor == 'K':
            sklep = wybierz_sklep(sklepy)
            sklep.zakupy()
        elif wybor == 'C':
            sklep = wybierz_sklep(sklepy)
            sklep.zmien_cennik()
        elif wybor == 'D':
            sklep = wybierz_sklep(sklepy)
            sklep.usun_towar()
        elif wybor == 'U':
            sklep = wybierz_sklep(sklepy)
            sklep.wypisz_utarg()
        else:
            print('Nieznana operacja')


if __name__ == '__main__':
    main()
