class Odmiana:
    def __init__(self, lowercase=False):
        # słowniki zawierają wpisy postaci 'Tadeusz': {'Tadeusza', 'Tadeuszowi', ...}
        # dla formy podstawowej pamięta zbiór odmian
        self._odmiany = {}
        # dla słowa odmienionego pamięta zbiór form podstawowych
        self._podstawowe = {}
        self._lowercase = lowercase

    def dodaj_wpis(self, podstawa, odmiana):
        if self._lowercase:
            podstawa = podstawa.lower()
            odmiana = odmiana.lower()
        if podstawa in self._odmiany:
            self._odmiany[podstawa].add(odmiana)
        else:
            self._odmiany[podstawa] = {odmiana}
        if odmiana in self._podstawowe:
            self._podstawowe[odmiana].add(podstawa)
        else:
            self._podstawowe[odmiana] = {podstawa}

    def znajdzOdmiany(self, slowo):
        if self._lowercase:
            slowo = slowo.lower()
        try:
            return self._odmiany[slowo]
        except KeyError:
            return set()

    def znajdzFormyPodstawowe(self, slowo):
        if self._lowercase:
            slowo = slowo.lower()
        try:
            return self._podstawowe[slowo]
        except KeyError:
            return set()

    def pierwszaFormaPodstawowa(self, slowo):
        '''Zwraca pierwszą formę podstawową dla danego słowa odmienionego.
           Jeśli słowo jest nieznane, to wynikiem jest to samo słowo.
           Takie działanie funkcji dobrze pasuje do zastosowania w liczeniu słów w pliku.
        '''
        for podstawa in self.znajdzFormyPodstawowe(slowo):
            return podstawa
        else:
            return slowo

    @staticmethod
    def wczytaj(sciezka="PoliMorf-0.6.7.tab", lowercase=False):
        baza = Odmiana(lowercase)
        with open(sciezka, encoding='utf-8') as plik:
            for linia in plik:
                t = linia.split()
                baza.dodaj_wpis(t[1], t[0])
        return baza
