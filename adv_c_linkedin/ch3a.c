#include <stdio.h>

int main(){
    printf("Enter an integer: ");
    int n;
    scanf("%d", &n);
    printf("\n\nYou entered: %.1f\n", (float)n);
    return(0);
}