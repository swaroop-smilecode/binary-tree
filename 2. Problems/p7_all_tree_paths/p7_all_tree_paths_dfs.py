def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  all_paths = []
  
  left_sub_paths = _all_tree_paths(root.left)
  for path in left_sub_paths:
    path.append(root.val)
    all_paths.append(path)

  right_sub_paths = _all_tree_paths(root.right)
  for path in right_sub_paths:
    path.append(root.val)
    all_paths.append(path)

  return all_paths


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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
