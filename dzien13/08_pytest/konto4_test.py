import pytest

from konto import Konto, BrakSrodkow

# To jest klasyczne podjeście do tworzenia "fixture", czyli zestawu danych/obiektów używanych w teście.
# Tutaj te obiekty (w naszym przypadku po prostu konto)
# tworzymy jako atrybuty w obiekcie klasy testującej.
# Metoda setup_method (nazwa ma znaczenie) jest wykonywana przed każdym testem
# i w tej metodzie można ustawić atrybuty, które są używane w teście.

# To podejście najbardziej przypomina JUnit itp. frameworki testowania z innych języków.

class TestKonto:
    def setup_method(self):
        self.konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)

    def test_init(self):
        assert self.konto.numer == 1
        assert self.konto.wlasciciel == 'Ala'
        assert self.konto.saldo == 1000

    def test_init0(self):
        inne_konto = Konto(2, 'Ola')
        assert inne_konto.numer == 2
        assert inne_konto.wlasciciel == 'Ola'
        assert inne_konto.saldo == 0

    def test_wplata(self):
        self.konto.wplata(300)
        assert self.konto.saldo == 1300

    def test_wplata_ujemna(self):
        with pytest.raises(ValueError):
            self.konto.wplata(-100)
        assert self.konto.saldo == 1000

    def test_wyplata(self):
        self.konto.wyplata(400)
        assert self.konto.saldo == 600

    def test_wyplata_ujemna(self):
        with pytest.raises(ValueError):
            self.konto.wyplata(-100)
        assert self.konto.saldo == 1000

    def test_wyplata_brak_srodkow(self):
        with pytest.raises(BrakSrodkow, match='Brak środków na koncie nr 1. Żądano 1200, a jest 1000.'):
            self.konto.wyplata(1200)
        assert self.konto.saldo == 1000
