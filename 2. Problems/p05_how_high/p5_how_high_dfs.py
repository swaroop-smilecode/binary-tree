def how_high(node):
    if node is None:
        return -1
    return 1 + max(how_high(node.left), how_high(node.right))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

root = a
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(how_high(root)) # -> 2