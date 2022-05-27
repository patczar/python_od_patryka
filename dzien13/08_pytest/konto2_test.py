import pytest

from konto import Konto, BrakSrodkow

# W tej wersji, aby uniknąćpisania konto = Konto(...) na początku każdego testy,
# tworzenie przykładowego obiektu umieszczamy w jednej metodzie.
# To z tej metody kolejne testy będą pobierać ten obiekt.
# W tej wersji robię to "w stylu pytest", czyli w oparciu o dekorator.

@pytest.fixture
def konto():
    return Konto(numer=1, wlasciciel='Ala', saldo=1000)

# Teraz, gdy jakaś metoda testowa X posiada parametr o takiej nazwie Y, jak nazwa funkcji oznaczonej fixture,
# to do funkcji testującej X jest przekazywany wynik funkcji Y.
# Funkcja Y tworząca obiekt będzie uruchamiana za każdy razem. Nowy obiekt dla każdego testu.

def test_init(konto):
    assert konto.numer == 1
    assert konto.wlasciciel == 'Ala'
    assert konto.saldo == 1000

def test_init0():
    konto = Konto(2, 'Ola')
    assert konto.numer == 2
    assert konto.wlasciciel == 'Ola'
    assert konto.saldo == 0

def test_wplata(konto):
    konto.wplata(300)
    assert konto.saldo == 1300

def test_wplata_ujemna(konto):
    with pytest.raises(ValueError):
        konto.wplata(-100)
    assert konto.saldo == 1000

def test_wyplata(konto):
    konto.wyplata(400)
    assert konto.saldo == 600

def test_wyplata_ujemna(konto):
    with pytest.raises(ValueError):
        konto.wyplata(-100)
    assert konto.saldo == 1000

def test_wyplata_brak_srodkow(konto):
    with pytest.raises(BrakSrodkow, match='Brak środków na koncie nr 1. Żądano 1200, a jest 1000.'):
        konto.wyplata(1200)
    assert konto.saldo == 1000
