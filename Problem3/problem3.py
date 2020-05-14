import sys
from queue import PriorityQueue
from collections import deque

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
        self.left = None
        self.right = None
    
    def set_left(self, left):
        self.left = left

    def set_right(self,right):
        self.right = right

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None
    
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

# main function to perform Huffman encoding
# Average time complexity is O(n log n)
# Average space complexity is O(n)
def huffman_encoding(data):
    dictionary = generate_dictionary(data)
    q = generate_priority_queue(dictionary)
    tree = generate_huffman_tree(q)
    print(tree)
    

def huffman_decoding(data,tree):
    pass

huffman_encoding("AAAAAABCDDDDDDD")
# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))