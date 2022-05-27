import pytest

from konto import Konto, BrakSrodkow

def test_init():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    assert konto.numer == 1
    assert konto.wlasciciel == 'Ala'
    assert konto.saldo == 1000


def test_init0():
    konto = Konto(2, 'Ola')
    assert konto.numer == 2
    assert konto.wlasciciel == 'Ola'
    assert konto.saldo == 0

# TODO do klasy Konto dodaj metody wplata i wyplata
# w testach (każda w oddzielnym) opisz jak mają działać i uzupełnij implementację

def test_wplata():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    konto.wplata(300)
    assert konto.saldo == 1300

def test_wplata_ujemna():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(ValueError):
        konto.wplata(-100)
    assert konto.saldo == 1000

def test_wyplata():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    konto.wyplata(400)
    assert konto.saldo == 600

def test_wyplata_ujemna():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(ValueError):
        konto.wyplata(-100)
    assert konto.saldo == 1000

def test_wyplata_brak_srodkow():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(BrakSrodkow):
        konto.wyplata(1200)
    assert konto.saldo == 1000

def test_wyplata_brak_srodkow():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(BrakSrodkow):
        konto.wyplata(1200)
    assert konto.saldo == 1000
