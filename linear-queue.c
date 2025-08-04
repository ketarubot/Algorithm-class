#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void enqueue(int x);
void dequeue();
int size();
int empty();

int *queue;
int front = -1, rear = -1;
int length;
int main(void) {
    scanf("%d", &length);
    queue = malloc(sizeof(int) * length);

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
    /*
     size() == length로 하려 했으나,
     rear가 queue의 범위를 벗어났음에도 enqueue가 되었기에
     (아마 동적할당해서) 아래 조건을 유지
     */
    if (rear >= length-1) {
        printf("Queue is full\n");
    } else {
        queue[++rear] = x;
    }
}

void dequeue() {
    if (empty()) {
        printf("Queue is empty\n");
    } else {
        printf("%d\n", queue[++front]);
    }
}

int size() {
    return rear - front;
}

int empty() {
    return size()?0:1;
}