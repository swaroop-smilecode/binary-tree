from collections import deque

def bottom_right_value(root):
    queue = deque([root])    
    while queue:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)  
    return current_node.val

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(10)
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
#   11     10
#  / \      \
# 4   -2     1

print(bottom_right_value(root)) # -> 1
