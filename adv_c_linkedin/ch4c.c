#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct animal{
    char *name;
    int age;
    char *sound;
};

struct animal * load_animal(char **name, int age, char **sound){
    struct animal *new_animal = malloc(sizeof(struct animal));
    new_animal->name = *name;
    new_animal->age = age;
    new_animal->sound = *sound;
    return(new_animal);
}

void show_animal(struct animal *my_animal){
    printf("\nAnimal name: %sAnimal age: %d\nAnimal sound: %s",
        my_animal->name, my_animal->age, my_animal->sound);
}


int main(){
    struct animal *my_animal;
    char tmp[4];
    char name[32], *nameptr;
    char sound[32], *soundptr;
    int age;

    printf("Enter the animal's name: ");
    fgets(name, 32, stdin);
    nameptr = name;
    printf("Enter the animal's age: ");
    fgets(tmp, 4, stdin);
    sscanf(tmp, "%d", &age);

    printf("Enter the animal's sound: ");
    fgets(sound, 32, stdin);
    soundptr = sound;
    my_animal = load_animal(&nameptr, age, &soundptr);
    show_animal(my_animal);

    return(0);
}