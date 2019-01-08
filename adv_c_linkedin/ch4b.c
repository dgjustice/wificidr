#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXLEN 32

void convert(char *str){
    for (int i=0; i < strlen(str); i++){
        if (isalpha(str[i])){
            str[i] = toupper(str[i]);
        }
        if (isspace(str[i])){
            str[i] = '-';
        }
    }
}

int main(){
    printf("Enter a string to be converted (up to %d chars): ", MAXLEN - 1);
    char str[MAXLEN];
    fgets(str, MAXLEN, stdin);
    convert(str);
    printf("\nThe converted string: %s", str);
    printf("\n");
    return(0);
}