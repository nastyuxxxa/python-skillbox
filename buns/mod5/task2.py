class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None
        else:
            temp = self.first.data
            self.first = self.first.next
            self.first.prev = None
            return temp

    def print(self):
        current = self.first
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
