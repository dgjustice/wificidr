#include <stdio.h>

int main(){
    printf("Please enter a number: ");
    float n;
    scanf("%f",&n);
    printf("\n%4.2f * 5 = ", n);
    printf("%4.2f", n *= 5);
    printf("\n%4.2f * 5 / 3 = ", n);
    printf("%4.2f\n", n /= 3);
    return(0);
}