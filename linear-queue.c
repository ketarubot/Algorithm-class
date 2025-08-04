#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void enqueue(int x);
void dequeue();

int *queue;
int front = -1, rear = -1;
int length;
int main(void) {
    scanf("%d", &length);
    queue = malloc(sizeof(int) * length);

    // enqueue {x}, dequeue 이외의 입력은 모두 종료
    while (1) {
        char cmd[11];
        scanf("%s", cmd);
        if (strcmp(cmd, "enqueue") == 0) {
            int num;
            scanf("%d", &num);
            enqueue(num);
        } else if (strcmp(cmd, "dequeue") == 0) {
            dequeue();
        } else break;
    }
    free(queue);
}

void enqueue(int x) {
    if (rear >= length-1) {
        printf("Queue is full\n");
    } else {
        queue[++rear] = x;
    }
}

void dequeue() {
    if (front+1 > rear) {
        printf("Queue is empty\n");
    } else {
        printf("%d\n", queue[++front]);
    }
}