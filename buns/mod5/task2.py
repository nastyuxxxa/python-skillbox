class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def dequeue(self):
        if self.start is None:
            return None
        else:
            temp = self.start.data
            self.start = self.start.next
            self.start.prev = None
            return temp

    def enqueue(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node

    def insert(self, n, val):
        if n <= 0 or self.start is None:
            self.enqueue(val)
            return
        new_node = Node(val)
        current_node = self.start
        for _ in range(n - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                break
        new_node.prev = current_node
        new_node.next = current_node.next
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        if new_node.next is None:
            self.end = new_node

    def print(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
