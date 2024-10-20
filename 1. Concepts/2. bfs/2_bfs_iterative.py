from collections import deque

def breadth_first_values(root_node):
    if not root_node:
     return []
    
    queue = deque([root_node])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)   
        if node.right:
            queue.append(node.right)

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


result = breadth_first_values(root_node)
print(result)