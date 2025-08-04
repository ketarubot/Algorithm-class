#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void push(int x);
void pop();
int size();
int empty();

int *stack;
int top = -1;
int length;
int main(void) {
    scanf("%d", &length);
    stack = malloc(sizeof(int) * length);

    // push {x}, pop, size, empty 이외의 입력은 모두 종료
    while (1) {
        char cmd[11];
        scanf("%10s", cmd);
        if (strcmp(cmd, "push") == 0) {
            int src;
            scanf("%d", &src);
            push(src);
        } else if (strcmp(cmd, "pop") == 0) {
            pop();
        } else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", size());
        } else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", empty());
        }else break;
    }
    free(stack);
}

void push(int x) {
    if (size() == length) {
        printf("Stack is full\n");
    } else {
        stack[++top] = x;
    }
}

void pop() {
    if (empty()) {
        printf("Stack is empty\n");
    } else {
        printf("%d\n", stack[top--]);
    }
}

int size() {
    return top+1;
}

int empty() {
    return size()?0:1;
}