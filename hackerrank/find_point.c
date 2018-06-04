#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

/*
 * Complete the findPoint function below.
 */

/*
 * Please store the size of the integer array to be returned in result_count pointer. For example,
 * int a[3] = {1, 2, 3};
 *
 * *result_count = 3;
 *
 * return a;
 *
 */
int* findPoint(int px, int py, int qx, int qy, int* result_count) {
    /*
     * Write your code here.
     */
    *result_count = 2;
    int *result = malloc(sizeof(int) * *result_count);
    result[0] = (-1 * px) + (2 * qx);
    result[1] = (-1 * py) + (2 * qy);
    return result;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int n_itr = 0; n_itr < n; n_itr++) {
        char** pxPyQxQy = split_string(readline());

        char* px_endptr;
        char* px_str = pxPyQxQy[0];
        int px = strtol(px_str, &px_endptr, 10);

        if (px_endptr == px_str || *px_endptr != '\0') { exit(EXIT_FAILURE); }

        char* py_endptr;
        char* py_str = pxPyQxQy[1];
        int py = strtol(py_str, &py_endptr, 10);

        if (py_endptr == py_str || *py_endptr != '\0') { exit(EXIT_FAILURE); }

        char* qx_endptr;
        char* qx_str = pxPyQxQy[2];
        int qx = strtol(qx_str, &qx_endptr, 10);

        if (qx_endptr == qx_str || *qx_endptr != '\0') { exit(EXIT_FAILURE); }

        char* qy_endptr;
        char* qy_str = pxPyQxQy[3];
        int qy = strtol(qy_str, &qy_endptr, 10);

        if (qy_endptr == qy_str || *qy_endptr != '\0') { exit(EXIT_FAILURE); }

        int result_count;
        int* result = findPoint(px, py, qx, qy, &result_count);

        for (int result_itr = 0; result_itr < result_count; result_itr++) {
            fprintf(fptr, "%d", result[result_itr]);

            if (result_itr != result_count - 1) {
                fprintf(fptr, " ");
            }
        }

        fprintf(fptr, "\n");
    }

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
