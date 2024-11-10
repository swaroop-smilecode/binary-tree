#### What is BFS?
- BFS means, Breadth First Search</br>
- It is implemented using `Queue`.</br>
- Because of this queue data structure, for example, when we start exploration at the root node,</br>
  if we need to do any work at that root node, will do that & then the left node & right node are pushed into Queue.</br>
  since queue operates in First In First Out manner, exploration happens in Breadth i.e. root --> it's left node --> it's right node.
#### Ways of implementing bfs algorithm
It is implemented in Iterative approach(By using Queue data structure).
#### Queue data structure
- In Queue data structure, data is added from right side & popped from left side - hence, FIFO
- Think of Queue as waiting in the line of grocery store.
- To add the data: append()
- To pop the data: popleft()
#### Time & Space complexity for Iterative approach
n = number of nodes
Time: O(n)
Space: O(n)
