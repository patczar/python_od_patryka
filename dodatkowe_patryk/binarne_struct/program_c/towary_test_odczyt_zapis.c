#include <stdio.h>
#include <stdlib.h>
#include "towar.h"
#include "err.h"

int main(int argc, char **argv) {
	printf("Startujemy\n");
	
	char* wejscie = argc >= 3 ? argv[1] : "towary.dat";
	char* wyjscie = argc >= 3 ? argv[2] : "towary2.dat";
	
	int ile_towarow;
	Towar *towary;
	odczytaj_plik_towary(wejscie, &towary, &ile_towarow);
	printf("Odczytałem %d towarów\n", ile_towarow);
	for(int i = 0; i < ile_towarow; i++) {
		towary[i].stan += 3;
		wypisz_towar(towary+i);
	}
	printf("Zapisuję...\n");
	zapisz_plik_towary(wyjscie, towary, ile_towarow);
	
	free(towary);
	printf("Koniec\n");
	return 0;
}
