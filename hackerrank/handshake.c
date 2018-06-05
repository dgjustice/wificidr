#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Complete the handshake function below.
 */
int handshake(int n) {
    /*
     * Write your code here.
     */
    int o;
    o = (n)*(n - 1)/2;
    return o;
}

int main()
{
    int arr[3] = {1, 3, 10};
    for (int i; i < 3; i++) {
        printf("%d -> %d\n", arr[i], handshake(arr[i]));
    }
    return 0;
}
