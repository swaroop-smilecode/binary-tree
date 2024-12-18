def path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [ root.val, *left_path ]
  
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [ root.val, *right_path ]
  
  return None

        
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

print(path_finder(root, 'e')) # -> [ 'a', 'b', 'e' ]