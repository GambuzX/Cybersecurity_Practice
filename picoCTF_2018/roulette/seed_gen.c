#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

const int MAX = 36;

int main(int argc, char * argv[]) {

	if (argc != 3) {
		printf("Usage: <executable> <seed> <n>\n");
		exit(0);
	}


	srand(atoi(argv[1]));

	for (int i = 0; i < atoi(argv[2]); i++) {
		printf("%d\n", (rand() % MAX) + 1);
	}	

	return 0;
}