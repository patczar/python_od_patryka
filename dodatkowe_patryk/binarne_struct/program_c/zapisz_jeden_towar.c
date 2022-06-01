#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include "towar.h"
#include "err.h"

// Zapisuje do pliku tylko jeden rekord Towar
int main(int argc, char **argv) {
	if(argc < 2) {
		fatal("Za malo argumentow, podaj nazwę pliku\n");
	}

	int fd = open(argv[1], O_WRONLY | O_CREAT, 0644);
	if(fd == -1)
		syserr("open");
	
	Towar towar;
	zainicjuj_towar(&towar, "Pralka", 1250, 10);
    zapisz_towar(fd, &towar);
	close(fd);
}
