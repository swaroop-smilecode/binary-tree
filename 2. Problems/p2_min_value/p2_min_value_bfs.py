from collections import deque

def tree_min_value(root):
    queue = deque([root])
    smallest = float("inf")
    while queue:
        current_node = queue.popleft()
        smallest = min(smallest, current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return smallest

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

root = a
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_min_value(root)) # -> -2