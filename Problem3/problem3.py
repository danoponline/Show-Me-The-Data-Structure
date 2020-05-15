import sys
from queue import PriorityQueue
from collections import deque

# Use regular Queue for tree representation only
class Queue:
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)

class Node:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.visited = False
        self.left = None
        self.right = None
        self.parent = None
        self.bit = None
    
    def set_left(self, left):
        self.left = left

    def set_right(self,right):
        self.right = right

    def set_parent(self,node):
        self.parent = node
    
    def set_visited(self):
        self.visited = True
    
    def set_bit(self,bit):
        self.bit = bit

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_parent(self):
        return self.parent

    def get_bit(self):
        return self.bit

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __eq__(self, other):
        return self.frequency == other.frequency
    
    def __gt__(self, other):
        return self.frequency > other.frequency

    def __lt__(self,other):
        return self.frequency < other.frequency

class Tree:
    def __init__(self):
        self.root = None
    
    def set_root(self,node):
        self.root = node

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        
        # Generate visit_order list as (node, level) for display
        while(len(q) > 0):
            node, level = q.deq()
            visit_order.append( (node, level) )
            if node is None:
                continue
            if node.has_left():
                q.enq( (node.get_left(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right():
                q.enq( (node.get_right(), level +1 ))
            else:
                q.enq( (None, level +1) )

        # Generate string for display
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                if node is None:
                    s += " | " + "<empty>"
                else:
                    s += " | " + format(node.value) + ":" + format(node.frequency)
            else:
                if node is None:
                    s += "\n" + "<empty>"
                else:
                    s += "\n" + format(node.value) + ":" + format(node.frequency)
                previous_level = level

        return s

# Help function to generate dictionary from string data
# Average time and space complexity is O(n)
def generate_dictionary(data):
    dictionary = {}
    for string in data:
        if string not in dictionary:
            dictionary[string] = 1
        else:
            dictionary[string] += 1
    return dictionary

# Help function to generate priority queue from dictionary
# Average time complexity is O(n log n)
# O(n) for outer loop through dictionary and 
# O(log n) for inner loop puting into the priority queue
# Average space complexity is O(n)
def generate_priority_queue(dictionary):
    q = PriorityQueue()
    for key in dictionary:
        q.put((dictionary[key], Node(key,dictionary[key])))
    return q

# Help function to generate middle node for creating Huffman tree
# Average time complexity is O(log n) to pop
# Average space complexity is O(1)
def generate_middle_node(q):
    freq_left, node_left = q.get()
    freq_right, node_right = q.get()
    middle_node = Node("middle", freq_left+freq_right)
    middle_node.set_left(node_left)
    middle_node.set_right(node_right)
    node_left.set_parent(middle_node)
    node_right.set_parent(middle_node)
    return middle_node

# Help function to generate root nood for creating Huffman tree
# Can only be used when there is exactly 4 elements in priority queue
# Average time complexity is O(log n) for generate_middle_node
# Average space complexity is O(1)
def generate_root_node(q):
    if q.qsize() != 4:
        print("This function is used to generate root node. Make sure to have 4 elements in the priority queue")
        return
    middle_node1 = generate_middle_node(q)
    middle_node2 = generate_middle_node(q)
    root = Node("root", middle_node1.frequency + middle_node2.frequency)
    if middle_node1 < middle_node2:
        root.set_left(middle_node1)
        root.set_right(middle_node2)
    else:
        root.set_left(middle_node2)
        root.set_right(middle_node1)
    middle_node1.set_parent(root)
    middle_node2.set_parent(root)
    return root

# Help function to generate Huffman tree
# Average time complexity is O(n log n)
# O(n) for outer loop poping almost every element in priority queue
# O(log n) for inner loop inserting element back into the queue
# Average space complexity is O(n)
def generate_huffman_tree(q):
    
    tree = Tree()
    
    # Generate tree for corner cases when q is empty up to qsize = 4
    if q.empty():
        return tree
    elif q.qsize() == 1:
        _, root = q.get()
        tree.set_root(root)
        return tree

    elif q.qsize() == 2:
        root = generate_middle_node(q)
        tree.set_root(root)
        return tree

    elif q.qsize() == 3:
        middle_node = generate_middle_node(q)
        q.put((middle_node.frequency, middle_node))
        root = generate_middle_node(q)
        tree.set_root(root)
        return tree

    elif q.qsize() == 4:
        root = generate_root_node(q)
        tree.set_root(root)
        return tree

    # Generate tree for regular case when qsize > 4
    else: # qsize > 4
        while q.qsize() > 4:
            middle_node = generate_middle_node(q)
            q.put((middle_node.frequency, middle_node))
    
        # Now q.qsize() == 4
        root = generate_root_node(q)
        tree.set_root(root)
        return tree

# Help function to generate encoding dictionary from Huffman tree
# Average time complexity is O(n log n)
# O(n) for outer recursion to go through all nodes
# O(log n) for inner while loop to traverse back to root
# in order to read all encoding bits
# Average space complexity is O(n)
def generate_encoding_dictionary(tree):
    dictionary = {}
    root = tree.get_root()
    
    # Corner case for root is the only leaf
    if root.is_leaf():
        dictionary[root.value] = str(0)
        return dictionary
    
    # Traverse all the node in the tree. Set child bit to 0 or 1 
    # for the left and right child, respectively
    def traverse_tree(node):
        
        # Found left node
        if node.has_left():
            node.get_left().set_bit(0)
            traverse_tree(node.get_left())
        
        # Found right node
        if node.has_right():
            node.get_right().set_bit(1)
            traverse_tree(node.get_right())
        
        # This is a leaf node
        if node.is_leaf():
            leaf_node = node
            key = node.value
            s = ""
            # Traverse back up the parents to generate encoding key
            while node.get_bit() is not None:
                s = str(node.get_bit()) + s
                node = node.get_parent()
            dictionary[key] = s
            node = leaf_node
            return dictionary
        return dictionary

    return traverse_tree(root)

# Help function to generate decoding dictionary from Huffman tree
# Average time complexity is O(n log n)
# O(n) for outer recursion to go through all nodes
# O(log n) for inner while loop to traverse back to root
# in order to read all decoding bits
# Average space complexity is O(n)
def generate_decoding_dictionary(tree):
    dictionary = {}
    root = tree.get_root()
    
    # Corner case for root is the only leaf
    if root.is_leaf():
        dictionary["0"] = str(root.value)
        return dictionary
    
    # Traverse all the node in the tree. Set child bit to 0 or 1 
    # for the left and right child, respectively
    def traverse_tree(node):
        
        # Found left node
        if node.has_left():
            node.get_left().set_bit(0)
            traverse_tree(node.get_left())
        
        # Found right node
        if node.has_right():
            node.get_right().set_bit(1)
            traverse_tree(node.get_right())
        
        # This is a leaf node
        if node.is_leaf():
            leaf_node = node
            value = node.value
            s = ""
            # Traverse back up the parents to generate encoding key
            while node.get_bit() is not None:
                s = str(node.get_bit()) + s
                node = node.get_parent()
            dictionary[s] = value
            node = leaf_node
            return dictionary
        return dictionary

    return traverse_tree(root)

# Main function to perform Huffman encoding
# Average time complexity is O(n log n)
# Average space complexity is O(n)
def huffman_encoding(data):
    if data is None or len(data) == 0 or not isinstance(data,str):
        print("Invaid data")
        return None, None
    dictionary = generate_dictionary(data)
    q = generate_priority_queue(dictionary)
    tree = generate_huffman_tree(q)
    dictionary = generate_encoding_dictionary(tree)
    encoded_data = ""
    for char in data:
        encoded_data += dictionary[char]
    return encoded_data, tree

# Main function to perform Huffman decoding
# Average time complexity is O(n log n)
# Average space complexity is O(n)
def huffman_decoding(data,tree):
    if data is None or len(data) == 0 or not isinstance(data,str):
        print("Invaid data")
        return None, None
    dictionary = generate_decoding_dictionary(tree)
    s = ""
    decoded_data = ""
    for string in data:
        s += string
        if s in dictionary:
            decoded_data += dictionary[s]
            s = ""
    return decoded_data

# Testing
if __name__ == "__main__":
    codes = {}

    print("Test 1: Print a great sentence: The bird is the word")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Expected Output: 

    # The size of the data is: 69

    # The content of the data is: The bird is the word

    # The size of the encoded data is: 36

    # The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

    # The size of the decoded data is: 69

    # The content of the encoded data is: The bird is the word

    print("\n-----------------------------------------------------------------------\n")

    print("Test 2: Print one character")
    a_great_sentence = "A"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Expected Output:

    # The size of the data is: 50

    # The content of the data is: A

    # The size of the encoded data is: 24

    # The content of the encoded data is: 0

    # The size of the decoded data is: 50

    # The content of the encoded data is: A

    print("\n-----------------------------------------------------------------------\n")

    print("Test 3: Empty input")
    a_great_sentence = ""
    _, _ = huffman_encoding(a_great_sentence)

    # Expected Output:
    # Invalid data

    print("\n-----------------------------------------------------------------------\n")

    print("Test 4: Print another great sentence: I am soooooooooo good")
    a_great_sentence = "I am soooooooooo good"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Expected Output:

    # The size of the data is: 70

    # The content of the data is: I am soooooooooo good

    # The size of the encoded data is: 32

    # The content of the encoded data is: 1000011001101101000111111111111111111110110101111001

    # The size of the decoded data is: 70

    # The content of the encoded data is: I am soooooooooo good
    print("\n-----------------------------------------------------------------------\n")