#include <stdio.h>

int main(){
    printf("Enter an integer: ");
    int n;
    scanf("%d", &n);
    printf("\nThe number you entered is ");
    (n % 2 == 0) ? printf("even.\n") : printf("odd.\n");
    return(0);
}