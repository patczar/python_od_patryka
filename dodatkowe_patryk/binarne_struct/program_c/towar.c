#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "err.h"
#include "towar.h"

/** Do rekordu Towar wpisuje podane wartości. */
void zainicjuj_towar(Towar *towar, const char *nazwa, int cena, int stan) {
	strncpy(towar->nazwa, nazwa, DLUGOSC_NAZWY_TOWARU);
	towar->cena = cena;
	towar->stan = stan;
}

/** Wypisuje towar na konsolę. */
void wypisz_towar(const Towar *towar) {
	printf("towar: %s, cena: %d, stan: %d\n", towar->nazwa, towar->cena, towar->stan);
}

void odczytaj_towar(int fd, Towar *towar) {
	if(read(fd, towar, sizeof(Towar)) == -1)
		syserr("read 1");	
}

void zapisz_towar(int fd, const Towar *towar) {
	if(write(fd, towar, sizeof(Towar)) == -1)
		syserr("write 1");	
}

/* Alokuje tablicę towarów i wspisuje wskaźnik do niej pod wskaznik_do_tablicy, a rozmiar pod zmienną rozmiar_tablicy.
 * Wywołujący jest odpowiedzialny za zwolnienie tablicy. */
void odczytaj_plik_towary(const char *plik, Towar **wskaznik_do_tablicy, int *rozmiar_tablicy) {
	int fd = open(plik, O_RDONLY, 0);
	if(fd < 0) {
		syserr("open w odczytaj_plik_towary, plik = %s", plik);
	}
	
	if(read(fd, rozmiar_tablicy, sizeof(int)) < 0) {
		syserr("read rozmiar w odczytaj_plik_towary");
	}
	
	Towar *towary = (Towar*)malloc(*rozmiar_tablicy * sizeof(Towar));
	if(towary == NULL) {
		syserr("malloc w odczytaj_plik_towary, rozmiar = %d", *rozmiar_tablicy);
	}
	*wskaznik_do_tablicy = towary;
	
	for(int i = 0; i < *rozmiar_tablicy; i++) {
		if(read(fd, towary+i, sizeof(Towar)) < 0) {
			syserr("read Towar w odczytaj_plik_towary, i = %d", i);
		}
	}
	
	if(close(fd) == -1) {
		syserr("close w odczytaj_plik_towary, fd = %d", fd);
	}
}

void zapisz_plik_towary(const char *plik, Towar *towary, int rozmiar_tablicy) {
	int fd = open(plik, O_WRONLY | O_CREAT, 0644);
	if(fd < 0) {
		syserr("open w zapisz_plik_towary, plik = %s", plik);
	}
	
	if(write(fd, &rozmiar_tablicy, sizeof(int)) < 0) {
		syserr("write rozmiar w zapisz_plik_towary");
	}

	for(int i = 0; i < rozmiar_tablicy; i++) {
		if(write(fd, towary+i, sizeof(Towar)) < 0) {
			syserr("write Towar w odczytaj_plik_towary, i = %d", i);
		}
	}

	if(close(fd) == -1) {
		syserr("close w zapisz_plik_towary, fd = %d", fd);
	}
}
