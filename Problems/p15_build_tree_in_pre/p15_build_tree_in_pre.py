class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_pre(in_order, pre_order):
    if len(in_order) == 0 or len(pre_order) == 0:
      return None
    
    # In pre_order data, root node is present at the left most side. Grab it.
    value = pre_order[0]
    root = Node(value)

    # Grab the left_in_order_data & right_in_order_data
    mid = in_order.index(value)
    left_in_order_data = in_order[:mid]
    right_in_order_data = in_order[mid + 1:]

    # Now, recognize the below facts:
    # len(left_in_order_data) == len(left_pre_data)
    # len(right_in_order_data) == len(right_pre_data)
    # So, let's prepare the left_pre_data & right_pre_data
    left_pre_data = pre_order[1:len(left_in_order_data)+1] # 1 is added at the end, because you did not started at 0, but at 1
    right_pre_data = pre_order[len(left_in_order_data)+1:]

    root.left = build_tree_in_pre(left_in_order_data, left_pre_data)
    root.right = build_tree_in_pre(right_in_order_data, right_pre_data)

    return root


print((
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
))
#       y
#    /    \
#   z      x