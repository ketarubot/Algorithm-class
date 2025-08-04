#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void push(int x);
void pop();

int *stack;
int rear = -1;
int length;
int main(void) {
    scanf("%d", &length);
    stack = malloc(sizeof(int) * length);

    // push {x}, pop 이외의 입력은 모두 종료
    while (1) {
        char cmd[11];
        scanf("%10s", cmd);
        if (strcmp(cmd, "push") == 0) {
            int src;
            scanf("%d", &src);
            push(src);
        } else if (strcmp(cmd, "pop") == 0) {
            pop();
        } else break;
    }
    free(stack);
}

void push(int x) {
    if (rear >= length-1) {
        printf("Stack is full\n");
    } else {
        stack[++rear] = x;
    }
}

void pop() {
    if (rear <= -1) {
        printf("Stack is empty\n");
    } else {
        printf("%d\n", stack[rear--]);
    }
}