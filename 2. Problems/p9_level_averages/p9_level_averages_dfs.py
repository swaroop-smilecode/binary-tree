from statistics import mean

def level_averages(root):
  levels = []
  fill_levels(root, levels, 0)
  
  avgs = []
  for level in levels:
    avgs.append(mean(level))
  return avgs
    
def fill_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  fill_levels(root.left, levels, level_num + 1)
  fill_levels(root.right, levels, level_num + 1)


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

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(level_averages(a)) # -> [ 3, 7.5, 1 ] 