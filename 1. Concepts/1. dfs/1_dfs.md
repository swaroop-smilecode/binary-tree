#### What is DFS?
--> DFS means, Depth First Search.</br>
--> If you want to explore the tree deeply(Until the base case is hit) in the path you firt step in,</br> 
    then it needs to be implemented using recursion.
    The reason is: Recursion uses stack data structure underneeth.</br>
    So, when you are travelling from root node to leaf nodes of the
    tree, work is not done during that travel, instead,</br>
    work is stored inside the stack & once recursive step hits the base case, 
    then the work starts executing from</br>
    leaf node to root node.</br>
--> That's why it is called Depth First Search.
#### Ways of implementing dfs algorithm
It can be implemented in 2 ways.
1. Recursive approach - when the same function is called in recursive step, stack is used.
2. Iterative approach - stack is implemented explicitly.</br>

**<ins>Note:</ins>**                                                   
But, at the end of the day, DFS means, always implement using Recursion. Do not go for Iterative approach & get confused.
#### Stack data structure
- In Stack data structure, data is added on top of exisitng data & when popped, the most recently stored data comes out.
- To add the data: append()
- To pop the data: pop()
#### Time & Space complexity for Iterative approach
n = number of nodes
Time: O(n)
Space: O(n)
#### Time & Space complexity for Recursive approach
n = number of nodes
Time: O(n^2)
Space: O(n)
