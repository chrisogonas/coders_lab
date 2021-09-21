"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self):
        self.i = 0
        self.node_string = None
        self.root = None
        self.my_list = []

    def serialize_tree(self, s_root):
        left = s_root.left
        if left is None:
            self.my_list.append('#')
        else:
            self.my_list.append(left)
            self.serialize_tree(left)

        right = s_root.right
        if right is None:
            self.my_list.append('#')
        else:
            self.my_list.append(right)
            self.serialize_tree(right)

        return self.my_list

    def deserialize_tree(self):
        if self.node_string is None:
            return None

        nodes = self.node_string.split(',')
        if nodes[self.i] == '#':
            return None
        else:
            return self.helper(nodes)

    def helper(self, arr):
        # print(self.i)
        if arr[self.i] == '#':
            return None

        h_root = TreeNode(arr[self.i])

        self.i += 1
        h_root.left = self.helper(arr)

        self.i += 1
        h_root.right = self.helper(arr)

        return h_root

    def in_order_traverse(self, i_root):
        if i_root is None:
            return None
        else:
            self.in_order_traverse(i_root.left)
            print(i_root.data, ' ')
            self.in_order_traverse(i_root.right)


node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')
node_f = TreeNode('f')
node_g = TreeNode('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

my_tree = BinaryTree()
my_tree.root = node_a

print('Serialization')
serialized = my_tree.serialize_tree(my_tree.root)
print(f'Serialized: {serialized}')
print(f'In Order Traversal: {my_tree.in_order_traverse(my_tree.root)}')

# my_nodes = ['b', 'd', '#', '#', 'e', '#', '#', 'c', 'f', '#', '#', 'g', '#', '#']
my_nodes = 'b,d,#,#,e,#,#,c,f,#,#,g,#,#'
my_tree.node_string = my_nodes
my_tree.deserialize_tree()

print()
print('Deserialization')
print(my_tree.root.data)
