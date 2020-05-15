# Huffman Coding

## Design Choices
1. Dictionary is used many places to hold characters as key and frequency as value
2. Dictionary is also used for lookup table for Huffman prefix code at both encoding and decoding sides
3. Priority queue is used so that the element that has highest priority will be popped out first (lowest frequency)
4. Tree is used to hold nodes. Each node has many data such as value(character), frequency, visited, left, right, parent, and bit (0 if this node is a left child with respect to the parent or 1 if a right child)
5. To obtain the Huffman code from a leaf node, traverse from a leaf to root and read each node's bit to construct the code


## Overall Average Complexity

The average time complexity for Huffmand Encoding and Decoding functions is O(n log n). The average space complexity for both functions is O(n). See problem3(dot)py for detail explannation at each section of the code.