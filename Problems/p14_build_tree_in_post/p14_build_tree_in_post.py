class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_post(in_order, post_order):
    if len(in_order) == 0 or len(post_order) == 0:
      return None
    
    # Let's create root node of the result tree.
    # We know that root node is the last value in the post_order traversal data.
    value = post_order[-1]
    root = Node(value)


    # Now, how should i initiate recursive calls?
    # Let's think:
    # I know that this root value is present exactly at the middle of in_order traversal data
    # Hence first i will grab that middle value index
    # Then, all the elements present left of that mid index are left_in_order traversal data -- count them
    # & the elements present at right of that mid index are the right_in_order traversal data -- count them.
    # Observe that in left_in_order & right_in_order traversal data, i am not considering mid value 
    # since it is already taken.
    mid = in_order.index(value)
    left_in_order_data = in_order[:mid]
    right_in_order_data = in_order[mid + 1:]

    # So, now you know how many elements are there in the left_in_order & right_in_order
    # The fact that should be recognized is: 
    # len(left_in_order) = len(left_post_order) 
    # len(right_in_order) = len(right_post_order)
    left_post_data = post_order[:len(left_in_order_data)]
    right_post_data = post_order[len(left_in_order_data):-1] # In post_order data, the last element is root node, that's why you exccluding it.

    # Let's make the recursive calls
    root.left = build_tree_in_post(left_in_order_data, left_post_data)
    root.right = build_tree_in_post(right_in_order_data, right_post_data)

    # At the end, i am returning the root node of the new tree formed.
    return root


print(build_tree_in_post(
  [ 'y', 'x', 'z' ],
  [ 'y', 'z', 'x' ] 
))
#       x
#    /    \
#   y      z