#include <stdio.h>

int main(){
    int n;
    int *a;
    a = &n;
    *a = 3;
    printf("n via *a: %d\n", *a);
    printf("increment : %d\n", ++*a);
    return(0);
}