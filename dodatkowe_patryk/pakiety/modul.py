# To jest przykład "modułu", czyli pliku, który może być imporotwany przez inne pliki (moduły, programy)

print('Początek modułu. Teraz __name__ == ', __name__)

MIASTO='Katowice'

def pole_kwadratu(a):
    return a*a


def wypisz_tekst(tekst, ile_razy):
    for i in range(ile_razy):
        print(tekst)

class Klasa:
    def metoda(self):
        print('To jest metoda')


if __name__ == '__main__':
    print('    O, teraz modul został uruchomiony jako program')
    wypisz_tekst('    __name__ == __main__', 2)
else:
    print('    Teraz moduł jest importowany')

print('Koniec modułu')
