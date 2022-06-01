#ifndef _TOWAR_H_
#define _TOWAR_H_

#define DLUGOSC_NAZWY_TOWARU 20
#define PLIK_TOWARY "towary.dat"

typedef struct towar {
	char nazwa[DLUGOSC_NAZWY_TOWARU];
	int cena;
	int stan;
} Towar;

extern void zainicjuj_towar(Towar *towar, const char *nazwa, int cena, int stan);

extern void wypisz_towar(const Towar *towar);

extern void odczytaj_towar(int fd, Towar *towar);

extern void zapisz_towar(int fd, const Towar *towar);

extern void odczytaj_plik_towary(const char *plik, Towar **wskaznik_do_tablicy, int *rozmiar_tablicy);

extern void zapisz_plik_towary(const char *plik, Towar *towary, int rozmiar_tablicy);

#endif
