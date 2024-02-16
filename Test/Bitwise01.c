#include <stdio.h>

int main() {
    int x = 12;

    printf("The ~x : %d\n", ~x);
    printf("The ~(~x) : %d\n", ~(~x));
}