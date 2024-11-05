class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_pre(in_order, pre_order):
  return _build_tree_in_pre(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_start, in_end, pre_start, pre_end):
  if in_end < in_start:
    return None
  value = pre_order[pre_start]
  root = Node(value)
  mid = in_order.index(value)
  left_size = mid - in_start
  root.left = _build_tree_in_pre(in_order, pre_order, in_start, mid - 1, pre_start + 1, pre_start + left_size)
  root.right = _build_tree_in_pre(in_order, pre_order, mid + 1, in_end, pre_start + left_size + 1, pre_end)
  return root


print((
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
))
#       y
#    /    \
#   z      x