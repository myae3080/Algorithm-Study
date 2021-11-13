// source : https://www.acmicpc.net/problem/10178
// math

#include <stdio.h>

int main() {
    int n, c, v, num1, num2;

    // input
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        // input
        scanf("%d %d", &c, &v);

        num1 = c / v;
        num2 = c % v;

        printf("You get %d piece(s) and your dad gets %d piece(s).\n", num1, num2);
    }

    return 0;
}