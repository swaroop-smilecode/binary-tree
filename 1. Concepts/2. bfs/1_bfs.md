#### What is BFS?
--> BFS means, Breadth First Search</br>
--> It is implemented using Queue. The reason is: when the tree is explored from root node to leaf node,</br> 
    work is done during the time of travel itself.</br>
    Where as in case of DFS, the work is stored in Stack & executed when the base case gets hit.</br>
    Because of this, the exploration happens in single path so deeply until the dead end(base case) is reached.</br>
--> Because of this Queue data structure, for example, when we start exploration at the root node,</br>
    the work is done at the root node, left node & right node are pushed into Queue.</br>
    Since left node is pushed first --> Work is done at left node & then it's left node & right node are pushed into Queue.</br>
    Since right node pushed second --> Work is done at right node & then it's left node & right node are pushed into Queue.</br>    
    So, the exploration happens in Breadth i.e. root --> it's left node --> it's right node.
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
