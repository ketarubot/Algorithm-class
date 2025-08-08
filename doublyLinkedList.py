from linkNode import DoubleNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        new_node = DoubleNode(data)
        if index == 0:
            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            self.append(data)
            return
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            prev_node = node.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = node
            node.prev = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def pop(self):
        if self.size == 0:
            raise ValueError("List is empty")
        self.delete(self.size - 1)

    def popleft(self):
        if self.size == 0:
            raise ValueError("List is empty")
        self.delete(0)

    def print(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print("None")

test = DoublyLinkedList()
