#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include "towar.h"
#include "err.h"

void zapisz_towar_parametry(int fd, const char *nazwa, int cena, int stan) {
	Towar towar;
	zainicjuj_towar(&towar, nazwa, cena, stan);
	zapisz_towar(fd, &towar);
}

int main(int argc, char **argv) {
	if(argc < 2) {
		fatal("Za malo argumentow, podaj nazwę pliku\n");
	}

	int fd = open(argv[1], O_WRONLY | O_CREAT, 0644);
	if(fd == -1)
		syserr("open");
	
	int rozmiar = 6;
	
	if(write(fd, &rozmiar, sizeof(int)) == -1)
		syserr("write 0");
	
	zapisz_towar_parametry(fd, "Pralka", 1200, 5);
	zapisz_towar_parametry(fd, "Odkurzacz", 250, 20);
	zapisz_towar_parametry(fd, "Telewizor", 2000,15);
	zapisz_towar_parametry(fd, "Kuchenka", 1500, 10);
	zapisz_towar_parametry(fd, "Zelazko", 300, 30);
	zapisz_towar_parametry(fd, "Czajnik", 219, 10);

	close(fd);
}
