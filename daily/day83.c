#include <stdlib.h>
#include <errno.h>
#include <stdio.h>
#include <time.h>

#define MAX_SIZE 1000

struct Node{
    char val;
    struct Node *left;
    struct Node *right;
};

void add_node(struct Node **node, char v)
{
    struct Node *new_item = malloc(sizeof(struct Node));
    if(!new_item) {
        perror("Couldn't allocate memory");
        exit(EXIT_FAILURE);
    }
    new_item->val = v;
    new_item->left = NULL;
    new_item->right = NULL;
    *node = new_item;
    return;
}

int is_empty(struct Node *node)
{
    return (node) ? 0: -1;
}

int has_child(struct Node *node)
{
    return (node->left) || (node->right);
}

// This could be more dynamic, but I'm a C n00b, so the array is easier
struct Node **dfs(struct Node *root)
{
    struct Node *node = root;
    struct Node *next_node;
    struct Node *pending[MAX_SIZE];
    struct Node **output = (struct Node **)malloc(MAX_SIZE * sizeof(struct Node*));
    int i, c;
    i = c = 0;

    for (int j=0; j<MAX_SIZE; j++)
        output[j] = NULL;

    while (node) {
        next_node = NULL;
        if (node->right){
            pending[i] = node->right;
            i++;
            if (i > MAX_SIZE) {
                perror("Stack overflow!\n");
                exit(EXIT_FAILURE);
            }
        }
        if (node->left) {
            next_node = node->left;
        } else {
            if (i){
                next_node = pending[i - 1];
                i--;
            }
        }
        output[c] = node;
        c++;
        node = next_node;
    }
    return output;
}

// void free_tree(struct Node *root)
// {
//     struct Node *node = root;
//     struct Node *next_node;
//     struct Node *pending[MAX_SIZE];
//     int i = 0;
//     while (node) {
//         next_node = NULL;
//         if (node->right){
//             pending[i] = node->right;
//             i++;
//             if (i > MAX_SIZE) {
//                 perror("Stack overflow!\n");
//                 exit(EXIT_FAILURE);
//             }
//         }
//         if (node->left) {
//             next_node = node->left;
//         } else {
//             if (i){
//                 next_node = pending[i - 1];
//                 i--;
//             }
//         }
//         free(node);
//         node = next_node;
//     }
//     return;
// }

void free_tree(struct Node *root)
{
    struct Node **node = dfs(root);
    for (int i = 0; (i < MAX_SIZE) && (node[i]); i++){
        free(node[i]);
    }
}

// void flip_tree(struct Node *root)
// {
//     struct Node *node = root;
//     struct Node *next_node;
//     struct Node *pending[MAX_SIZE];
//     int i = 0;
//     while (node) {
//         next_node = NULL;
//         if (node->right){
//             pending[i] = node->right;
//             i++;
//             if (i > MAX_SIZE) {
//                 perror("Stack overflow!\n");
//                 exit(EXIT_FAILURE);
//             }
//         }
//         if (node->left) {
//             next_node = node->left;
//         } else {
//             if (i){
//                 next_node = pending[i - 1];
//                 i--;
//             }
//         }
//         struct Node * tmp = node->left;
//         node->left = node->right;
//         node->right = tmp;
//         node = next_node;
//     }
//     return;
// }

void flip_tree(struct Node *root)
{
    struct Node **node = dfs(root);
    struct Node *tmp;
    for (int i = 0; (i < MAX_SIZE) && (node[i]); i++){
        tmp = node[i]->left;
        node[i]->left = node[i]->right;
        node[i]->right = tmp;
    }
}

int main(int argc, char *argv[])
{
    struct Node *root;
    add_node(&root, 'a');
    add_node(&root->left, 'b');
    add_node(&root->right, 'c');
    add_node(&root->left->left, 'd');
    add_node(&root->left->right, 'e');
    add_node(&root->right->left, 'f');

    if (has_child(root)) printf("Root has children\n\n");
    if (has_child(root->right->left)) printf("This shouldn't print.\n\n");
    if (has_child(root->right)) printf("This should print.\n\n");

    if (is_empty(root)) printf("It's empty!\n");
    
    printf("root->left %c\n", root->left->val);
    printf("root->right %c\n", root->right->val);
    flip_tree(root);
    printf("These should be flipped...\n");
    printf("root->left %c\n", root->left->val);
    printf("root->right %c\n", root->right->val);

    printf("\n\nplay with the dfs \n\n");
    struct Node **test = dfs(root);
    for (int i = 0; (i < MAX_SIZE) && (test[i]); i++){
        printf("val in dfs %c\n", test[i]->val);
    }

    free_tree(root);
    return 0;
}
