#include <stdlib.h>
#include <errno.h>
#include <stdio.h>
#include <time.h>

struct Stack{
    int val;
    struct Stack *next_item;
};

struct Stack *create_stack()
{
    // Dummy function to start a new stack
    struct Stack *new_stack = NULL;
    return new_stack;
}

void die(const char *message)
{
    if(errno) {
        perror(message);
    } else {
        printf("ERROR: %s\n", message);
    }

    exit(1);
}

void push(struct Stack **stack, int v)
{
    struct Stack *new_item = malloc(sizeof(struct Stack));
    if(!new_item) die("Couldn't allocate more memory");
    new_item->val = v;
    new_item->next_item = *stack;
    *stack = new_item;
    return;
}

int pop(struct Stack **stack)
{
    int v = (*stack)->val;
    struct Stack *temp = *stack;
    *stack = (*stack)->next_item;
    free(temp);
    return v;
}

int is_empty(struct Stack **stack)
{
    if(!stack){
        return 0;
    } else {
        return -1;
    }
}

int main(int argc, char *argv[])
{
    srand(time(NULL));
    struct Stack *my_stack = create_stack();
    int i = 0;
    int v = 0;
    for(i = 0; i <= 1000; i++){
        v = rand() % 100;
        printf("Pushing %d to the stack\n", v);
        push(&my_stack, v);
        printf("Value int after push: %d\n", my_stack->val);
    }
    while(my_stack){
        printf("Popping last value from stack.\n");
        int t = pop(&my_stack);
        printf("Success! Returned: %d\n", t);
    }
    if(is_empty(&my_stack)) printf("It's empty!\n");
    return 0;
}
