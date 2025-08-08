class SingleNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev