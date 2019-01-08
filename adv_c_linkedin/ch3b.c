#include <stdio.h>

int *five_primes(){
    static int arr[] = {2, 3, 5, 7, 9};
    return arr;
}

int main(){
    int *arr = five_primes();
    for(int i=0; i < 5; i++){
        printf("%d\n", arr[i]);
    }
    return(0);
}