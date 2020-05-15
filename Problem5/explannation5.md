# Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Overall Average Complexity
The overall time complexity is O(1). Since we keep track of the tail, it takes constant time to add a new block. The space complexity is O(n) depending on how many block input we want to chain up.