#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

char flag[]  = "KID20{1_h4v3_b33n_f0unD}";

void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    _exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

int main() {
    ignore_me_init_buffering();
	ignore_me_init_signal();

   char *flagPointer = flag;
   char input[20];
   puts("Where to look?");
   fgets(input, 20, stdin);
   printf(input);
   return 0;
}