#include <stdio.h>
#include <stdlib.h>

int main() {
    int count, num1, num2;

    scanf("%d", &count);

    int *numArray = (int*)malloc(sizeof(int) * count);

    for (int i = 0; i < count; i++) {
        scanf("%d %d", &num1, &num2);
        numArray[i] = num1 + num2;
    }

    for (int i = 0; i < count; i++) {
        printf("%d\n", numArray[i]);
    }

    free(numArray);

    return 0;
}