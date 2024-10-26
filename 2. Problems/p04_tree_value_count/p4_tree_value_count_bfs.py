from collections import deque

def tree_value_count(root, target):
    count = 0
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        if current_node.val == target:
            count += 1
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return count


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
