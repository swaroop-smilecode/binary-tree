# Since we were creating new list using the syntax [ root.val, *left_path ] & [ root.val, *right_path ],
# This time we append to the existing list --> But, since appending to list adds at the end of list,
# we need to perform return result[::-1] at the time of returning final result.

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  
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