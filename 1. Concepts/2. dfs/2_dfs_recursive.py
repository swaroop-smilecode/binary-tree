def depth_first_values(root_node):
    if not root_node:
     return []
    
    right_values = depth_first_values(root_node.right)
    left_values = depth_first_values(root_node.left)
    return [root_node.val, *left_values, *right_values]


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

root_node = a
#     a
#    / \     
#   b   c
#  / \   \
# d   e   f


print(depth_first_values(root_node)) #['a', 'b', 'd', 'e', 'c', 'f']