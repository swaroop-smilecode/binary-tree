def flip_tree(root):
  if root is None:
    return None
  left = flip_tree(root.left)
  right = flip_tree(root.right)  
  root.left = right
  root.right = left
  return root

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
g = Node("g")
h = Node("h")

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

print(flip_tree(a)) # <__main__.Node object at 0x0000022E24E5BCE0> 

#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g