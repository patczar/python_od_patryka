import pytest

from konto import Konto, BrakSrodkow

class TestKonto:
    @pytest.fixture
    def konto(self):
        return Konto(numer=1, wlasciciel='Ala', saldo=1000)

    def test_init(self, konto):
        assert konto.numer == 1
        assert konto.wlasciciel == 'Ala'
        assert konto.saldo == 1000

    def test_init0(self):
        konto = Konto(2, 'Ola')
        assert konto.numer == 2
        assert konto.wlasciciel == 'Ola'
        assert konto.saldo == 0

    def test_wplata(self,konto):
        konto.wplata(300)
        assert konto.saldo == 1300

    def test_wplata_ujemna(self,konto):
        with pytest.raises(ValueError):
            konto.wplata(-100)
        assert konto.saldo == 1000

    def test_wyplata(self,konto):
        konto.wyplata(400)
        assert konto.saldo == 600

    def test_wyplata_ujemna(self,konto):
        with pytest.raises(ValueError):
            konto.wyplata(-100)
        assert konto.saldo == 1000

    def test_wyplata_brak_srodkow(self,konto):
        with pytest.raises(BrakSrodkow, match='Brak środków na koncie nr 1. Żądano 1200, a jest 1000.'):
            konto.wyplata(1200)
        assert konto.saldo == 1000
