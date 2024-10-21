from collections import deque

def tree_includes(root, target):
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        if current_node.val == target:
            return True
        else:
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return False


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

root = a
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(root, "e")) # -> True