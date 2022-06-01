#include <stdio.h>
#include <stdlib.h>
#include "towar.h"
#include "err.h"

int main(int argc, char **argv) {
	printf("Startujemy\n");
	char* wejscie = argc >= 2 ? argv[1] : "towary.dat";

	int ile_towarow;
	Towar *towary;
	odczytaj_plik_towary(wejscie, &towary, &ile_towarow);
	printf("Odczytałem %d towarów\n", ile_towarow);
	for(int i = 0; i < ile_towarow; i++) {
		wypisz_towar(towary+i);
	}
	
	free(towary);
	printf("Koniec\n");
	return 0;
}
