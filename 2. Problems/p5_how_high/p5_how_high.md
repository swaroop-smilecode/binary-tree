Height of the tree means, number of edges from root node to leaf node, along the longest path.
![image](https://github.com/user-attachments/assets/fe579785-61cf-43f7-80b0-455f0f1d82e9)

<ins>Base case:</ins></br>
What's the answer this solution should give when input is smallest(When there is no node)?</br>
When there is no node means --> node is None --> Consider this None node itself as a Tree & ask the question. What's the height of this tree?</br>
It's 0?</br>
No, it can't be 0, the reason is we saw the definition of height of the tree(Number of edges from root node to leaf node)</br>
When there is no edge, how can you say, it's 0?</br>
Also, Look at the code. If you consider 0, then the answer will be expected answer + 1</br>
Hence, considering -1 fits this situation.
![image](https://github.com/user-attachments/assets/b683d0e7-6597-48d3-8622-df9b507de132)
```python
def how_high(node):
  if node is None:
      return -1
```
<ins>Recursive step:</ins></br>
```python
def how_high(node):
  if node is None:
      return -1
  return 1 + max(how_high(node.left), how_high(node.right))
```
<ins>Complete solution:</ins></br>
```python
def how_high(node):
  if node is None:
      return -1
  return 1 + max(how_high(node.left), how_high(node.right))
```
