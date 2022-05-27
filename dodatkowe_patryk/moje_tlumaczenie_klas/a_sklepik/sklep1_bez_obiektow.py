# Gdybyśmy chcieli funkcjonalność podobną do przykładów sklep z dzien3 zrealizować z wykorzystaniem funkcji.

# Zauważmy, że przy tym podejściu dane, do których muszą mieć dostęp różne funkcje, tutaj cennik i utarg,
# są zmiennymi globalnymi.
# Zatem ten program jest w stanie obsłużyć jeden sklep, a nie kilka sklepów jednocześnie.

cennik = {
    'pralka': 2800,
    'lodówka': 3300,
    'czajnik': 424,
    'TV': 2500,
}

utarg = 0


def wypisz_cennik():
    print('Nasz asortyment:')
    for t, c in cennik.items():
        print(f'{t:10} : {c:6}')
    print()


def do_zaplaty(towar, sztuk=1):
    if towar in cennik:
        return cennik[towar] * sztuk
    else:
        raise KeyError(f'Nie istnieje produkt o nazwie {towar}')


def zakupy():
    global utarg

    towar = input('Podaj nazwę towaru: ')
    sztuk = int(input(f'Ile sztuk {towar} chcesz kupić? '))
    try:
        kwota = do_zaplaty(towar, sztuk)
        utarg += kwota
        print(f'Za {sztuk} sztuk towaru {towar} zapłacisz {kwota}')
    except KeyError as e:
        print(e)


def wypisz_utarg():
    # tutaj nie trzeba pisać global, bo tylko odczytujemy zmienną globalną
    print(f'Bieżący utarg: {utarg}')


def main():
    while True:
        print('\nWybierz operacje:')
        print(' Q - zakończ program')
        print(' P - wypisz cennik')
        print(' U - wypisz bieżący utarg sklepu')
        print(' K - zakupy')
        wybor = input(": ").strip().upper()
        if wybor == 'Q':
            break
        elif wybor == 'P':
            wypisz_cennik()
        elif wybor == 'K':
            zakupy()
        elif wybor == 'U':
            wypisz_utarg()
        else:
            print('Nieznana operacja')


if __name__ == '__main__':
    main()
