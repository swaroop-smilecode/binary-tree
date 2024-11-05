### For the first time, you may try to solve the problem as below.
```python
def build_tree_in_pre(in_order, pre_order):
    if len(in_order) == 0 or len(pre_order) == 0:
      return None
    
    value = pre_order[0]
    root = Node(value)

    mid = in_order.index(value)
    left_in_order_data = in_order[:mid]
    right_in_order_data = in_order[mid + 1:]

    left_pre_data = pre_order[1:len(left_in_order_data)+1]
    right_pre_data = pre_order[len(left_in_order_data)+1:]

    root.left = build_tree_in_pre(left_in_order_data, left_pre_data)
    root.right = build_tree_in_pre(right_in_order_data, right_pre_data)

    return root
```
### Let's improving the code
But, it's of `n^2` complexity, becasue the list slicing is used --> Whenever you do list slicing, it results in `O(n)` complexity.</br>
On top of this, if list slicing is used in recursive calls which are happning `O(n)` times, then in total, it results in `O(n^2)` complexity.

So, let's improve the code. Instead of passing the sliced list, will pass indexes.</br>
We know list index start with `0` & end with `len(list)`.</br> 
In the input we have 2 lists & we have to work on them from starting to ending of the lists.</br>
Hence, will initiate left pointer at index `0` & right pointer at index `len(in_order) -1` for in_order list
and in the same way, </br> 
will initiate left pointer at index `0` & right pointer at `len(pre_order) - 1` for pre_order list.
```python
def build_tree_in_pre(in_order, pre_order):
    return _build_tree_in_pre(in_order,
                              pre_order,
                              0,
                              len(in_order) - 1,
                              0,
                              len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_start, in_end, pre_start, pre_end):
    pass
```

### Let's see the base case:
When we are passing indexe of list as fn parameter instead of direct list itself, it means, 
we are workig on list indirectly through indexes.</br> 
We can use the word logical list in this case.

Logically, our array becomes empty when start pointer & end pointer crosses.</br>
Array becomes empty means, input is becoming smallest. Smallest input is the base case, isn't it?</br>
By the way, you should check for  `(in_end < in_start)` not `(in_end <= in_start)`, because when `in_end` == `in_start`,</br>
it's like we are working on the array of length `1`.
```python
def build_tree_in_pre(in_order, pre_order):
    return _build_tree_in_pre(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_start, in_end, pre_start, pre_end):
    if (in_end < in_start) or (pre_start < pre_end):
    return None
```
### It's time for recursive calls
```python
def build_tree_in_pre(in_order, pre_order):
    return _build_tree_in_pre(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_start, in_end, pre_start, pre_end):
    if (in_end < in_start) or (pre_start < pre_end):
        return None

    value = pre_order[pre_start]
    root = Node(value)
    mid = in_order.index(value)
    left_size = mid - in_start
    root.left = _build_tree_in_pre(in_order, pre_order, in_start, mid - 1, pre_start + 1, pre_start + left_size)
    root.right = _build_tree_in_pre(in_order, pre_order, mid + 1, in_end, pre_start + left_size + 1, pre_end)
```
