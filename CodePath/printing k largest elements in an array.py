"""
Question:
Write an efficient program for printing k largest elements in an array. Elements in an array can be in any order.
For example, if the given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3
then your program should print 50, 30, and 23.

UMPIRE

My preferred approach - plan/pseudocode:
1. sort -> insert to a tree
2. return k right-most branch items
"""

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert_child(self, child, data):
        if child is None:
            self.root = Node(data)
        elif child.data <= data:
            if child.left is None:
                child.left = Node(data)
            else:
                self.insert_child(child.left, data)
        else:
            if child.right is None:
                child.right = Node(data)
            else:
                self.insert_child(child.right, data)

    def print_bfs(self):
        pass

    def print_dfs(self):
        pass

    def print_k_largest(self):
        pass
