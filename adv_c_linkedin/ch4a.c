#include <stdio.h>
#include <ctype.h>

#define MAXLEN 32

void bsort(char *string){
    for(int i=0; (i < MAXLEN && isalnum(string[i])); i++){
        for(int j=i + 1; (j < MAXLEN && isalnum(string[j])); j++){
            if (string[i] > string[j]){
                char tmp = string[j];
                string[j] = string[i];
                string[i] = tmp;
            }
        }
    }
}

int main(){
    printf("Enter a string to be sorted (up to 32 chars): ");
    char str[MAXLEN];
    scanf("%s", str);
    bsort(str);
    printf("\nThe sorted string: %s", str);
    printf("\n");
    return(0);
}