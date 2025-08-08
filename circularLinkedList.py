from linkNode import SingleNode

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range')

        new_node = SingleNode(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        elif index == 0:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            self.head = new_node
            last.next = self.head
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node

        self.size += 1

    def append(self, data):
        new_node = SingleNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new_node
            new_node.next = self.head
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

        if index == 0:
            if self.size == 1:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.next = node.next.next

        self.size -= 1

    def pop(self):
        if self.head is None:
            raise ValueError('List is empty')

        curr = self.head
        prev = None
        while curr.next != self.head:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = None
        else:
            prev.next = self.head

        self.size -= 1

    def popleft(self):
        if self.head is None:
            raise ValueError('List is empty')
        self.delete(0)

    def print(self):
        if self.head is None:
            return
        node = self.head
        while True:
            print(node.data, end=' ')
            node = node.next
            if node == self.head:
                break
        print()

test = CircularLinkedList()
