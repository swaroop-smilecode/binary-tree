def depth_first_values(root_node):
    if not root_node:
     return []
    
    stack = [root_node]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)   
        if node.left:
            stack.append(node.left)

    return result


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


result = depth_first_values(root_node)
print(result)