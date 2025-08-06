#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void enqueue(int x);
void dequeue();
int size();
int empty();

int *queue;
int front = 0, rear = 0;
int length;
int main(void) {
    scanf("%d", &length);
    queue = malloc(sizeof(int) * (length+1));

    // enqueue {x}, dequeue, size, empty 이외의 입력은 모두 종료
    while (1) {
        char cmd[11];
        scanf("%s", cmd);
        if (strcmp(cmd, "enqueue") == 0) {
            int num;
            scanf("%d", &num);
            enqueue(num);
        } else if (strcmp(cmd, "dequeue") == 0) {
            dequeue();
        } else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", size());
        } else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", empty());
        } else break;
    }
    free(queue);
}

void enqueue(int x) {
    if (size() == length) {
        printf("Queue is full\n");
    } else {
        queue[rear%length] = x;
        rear = (rear+1)%(length+1);
    }
}

void dequeue() {
    if (empty()) {
        printf("Queue is empty\n");
    } else {
        printf("%d\n", queue[front%length]);
        front = (front+1)%(length+1);
    }
}

int size() {
    return
        front > rear ?
        length - front + rear :
        rear - front;
}

int empty() {
    return front == rear;
}