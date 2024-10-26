Height of the tree means, number of edges from root node to leaf node, along the longest path.
![image](https://github.com/user-attachments/assets/fe579785-61cf-43f7-80b0-455f0f1d82e9)

<ins>Base case:</ins></br>
What's the answer this solution should give when input is smallest(When there is no node)?</br>
When there is no node means --> node is None --> Consider this None node itself as a Tree & ask the question. What's the height of this tree?</br>
It's 0?</br>
No, it can't be 0, the reason is we saw the definition of height of the tree(Number of edges from root node to leaf node)</br>
When there is no edge, how can you say, it's 0?</br>
Also, Look at the code. If you consider 0, then the answer will be expected answer + 1</br>
Hence, considering -1 fits this situation. Let's see how</br>
Let's consider the first leaf node gets -1 & -1 from it's left child & right child
![image](https://github.com/user-attachments/assets/aad1664d-fb21-41bf-8037-b7c228c39e39)
max(left child value, right child value) = -1</br>
This -1 gets returned from the leaf node
![image](https://github.com/user-attachments/assets/ffa219f7-896b-4416-9230-18acf98f6690)
But, since you are crossing one node, 1 should be added to the returned value.</BR>
Which results in 0 --> Which is correctly indicating the max height of the tree as of now.
![image](https://github.com/user-attachments/assets/5b14f1ae-6c61-43cd-802c-c86053c9da30)
So,
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
