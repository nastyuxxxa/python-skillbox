class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.prev
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.prev = self.end
        self.end = new_node

    def print(self):
        current_node = self.end
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.prev
        print()
