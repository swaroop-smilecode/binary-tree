from collections import deque
def lefty_nodes(root):
    result = []
    queue = deque([(root, 0)])
    while queue:
        curr_node, level = queue.popleft()
        if len(result) == level:
            result.append(curr_node.val)
        if curr_node.left:
            queue.append((curr_node.left, level+1))
        if curr_node.right:
            queue.append((curr_node.right, level+1))            
    return result

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
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(lefty_nodes(a)) # [ 'a', 'b', 'd', 'g' ]