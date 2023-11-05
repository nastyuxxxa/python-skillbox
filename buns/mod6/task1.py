class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def get(self, index):
        if self.head is None:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value if current_node else None

    def remove(self, index):
        if index == 0:
            self.head = self.head.next if self.head else None
            return
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next

    def insert(self, n, value):
        new_node = Node(value)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(n - 1):
            current_node = current_node.next
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next