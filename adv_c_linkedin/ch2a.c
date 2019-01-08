#include <stdio.h>

int main(int argc, char** argv){
    printf("This program name is %s\n\n", argv[0]);
    if (argc == 2)
        printf("You only entered a single arg\n");
    for (int i=1; i < argc; i++){
        printf("%s\n", argv[i]);
    }
    
    return(0);
}