#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>


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

void win() {
    system("/bin/sh");
}

int main() {
    ignore_me_init_buffering();
    ignore_me_init_signal();

    char input[0x55];
    puts("Enter the magic number to win:");
    gets(input);
    if(strcmp(input, "31337") == 0) {
        puts("🎉🎉🎉🎉");
    }
    else {
        puts("Sorry :/");
    }
    return 0;
}