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
