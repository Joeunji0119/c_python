#include <stdio.h>
#pragma warning(disable:4996)

int a, b, c;
int product(int x, int y);

int main() {
    printf("Enter a number between 1 and 100 : ");
    scanf("%d", &a);

    printf("Enter a number between 1 and 100 : ");
    scanf("%d", &b);

    c = product(a,b);
    printf("%d * %d = %d \n", a, b, c);

    return 0;
}

int product(int x, int y){
    return (x * y);
}