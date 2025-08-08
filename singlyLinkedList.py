from linkNode import SingleNode

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if self.head is None:
            self.head = SingleNode(data)
            self.size += 1
            return

        if index < 0 or index > self.size:
            raise IndexError('Index out of range')

        if index == 0:
            temp = self.head
            self.head = SingleNode(data)
            self.head.next = temp
            self.size += 1
            return

        node = self.head
        temp = 0
        while temp < index - 1:
            temp += 1
            node = node.next
        new_node = SingleNode(data)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def append(self, data):
        self.size += 1

        if self.head is None:
            self.head = SingleNode(data)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = SingleNode(data)

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        temp = 0
        node = self.head
        while temp < index - 1:
            temp += 1
            node = node.next
        node.next = node.next.next
        self.size -= 1

    def pop(self):
        if self.head is None:
            raise ValueError('List is empty')

        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = None
        else:
            prev.next = None

        self.size -= 1

    def popleft(self):
        if self.head is None:
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    def print(self):
        if self.head is None:
            return
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print("None")

test = SinglyLinkedList()
