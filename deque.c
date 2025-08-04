#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void push_front(int x);
void push_rear(int x);
void pop_front();
void pop_rear();
int size();
int empty();

int *queue;
int front = -1, rear = -1;
int length;
int main(void) {
    scanf("%d", &length);
    queue = malloc(sizeof(int) * length);

    // push_front/back {x}, pop_front/back, size, empty 이외의 입력은 모두 종료
    while (1) {
        char cmd[11];
        scanf("%s", cmd);
        if (strcmp(cmd, "push_front") == 0) {
            int num;
            scanf("%d", &num);
            push_front(num);
        } else if (strcmp(cmd, "push_rear") == 0) {
            int num;
            scanf("%d", &num);
            push_rear(num);
        } else if (strcmp(cmd, "pop_front") == 0) {
            pop_front();
        } else if (strcmp(cmd, "pop_rear") == 0) {
            pop_rear();
        }else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", size());
        } else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", empty());
        } else break;
    }
    free(queue);
}

void push_front(int x) {
    if (front < 0) {
        printf("front is full. please try push rear\n");
    } else {
        queue[front--] = x;
    }
}

void push_rear(int x) {
    if (rear >= length-1) {
        printf("rear is full. please try push front\n");
    } else {
        queue[++rear] = x;
    }
}

void pop_front() {
    if (empty()) {
        printf("Deque is empty\n");
    } else {
        printf("%d\n", queue[++front]);
    }
}

void pop_rear() {
    if (empty()) {
        printf("Deque is empty\n");
    } else {
        printf("%d\n", queue[rear--]);
    }
}

int size() {
    return rear - front;
}

int empty() {
    return size()?0:1;
}