// source : https://www.acmicpc.net/problem/5522
// math

#include <stdio.h>

int main() {
    int n, total = 0;

    for (int i = 0; i < 5; i++) {
        scanf("%d", &n);
        total += n;
    }

    printf("%d", total);

    return 0;
}