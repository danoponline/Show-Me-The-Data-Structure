# LRU Cache

For this problem, dictionary with key = some number and value = a node in a doubly linked list. Every time data is set or acquired, a node is added/moved to the tail of the linked list to indicate that this node is just used. The head is the least recently used and is removed when the cache is full and a new data is arrived at the tail. Dictionary is used here for constant time O(1) access to easily indicate the used node and move it to the tail. There is no need to traverse along the linked list to find the used node.

The overall time and space complexity is O(1).