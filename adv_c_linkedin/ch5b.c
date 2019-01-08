#include <stdio.h>
#include <string.h>

int main(){
    char arr[] = "foo bar bang";
    char *arrptr = arr;
    int l = strlen(arrptr);
    for (int i=0; i < l; i++)
        putchar(*(arrptr + i));
    printf("\n");
    return(0);
}