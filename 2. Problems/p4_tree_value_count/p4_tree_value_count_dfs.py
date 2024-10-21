def tree_value_count(root, target):
    if root is None:
        return 0
    match = 1 if root.val == target else 0
    return match + (tree_value_count(root.left, target) + tree_value_count(root.right, target))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

root = a
#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

print(tree_value_count(root,  6)) # -> 3
