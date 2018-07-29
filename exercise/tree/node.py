class Node:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, element):
        pass