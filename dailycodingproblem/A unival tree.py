"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def value(self):
        return self.value


def count_univals(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif root.left.value == root.right.value:
        return 1
    elif not root.left and root.right:
        return count_univals(root.right)
    elif root.left and not root.right:
        return count_univals(root.left)

    univals = count_univals(root.left) + count_univals(root.right)

    return univals

node_a = Node('0')
node_b = Node('1')
node_c = Node('0')
node_d = Node('1')
node_e = Node('0')
node_f = Node('1')
node_g = Node('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

# assert count_univals(None) == 0
assert count_univals(node_a) == 5
# assert count_univals(node_c) == 4
assert count_univals(node_g) == 1
assert count_univals(node_d) == 3