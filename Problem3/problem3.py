import sys
from queue import PriorityQueue

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

def generate_dictionary(data):
    dictionary = {}
    for string in data:
        if string not in dictionary:
            dictionary[string] = 1
        else:
            dictionary[string] += 1
    return dictionary

def generate_priority_queue(dictionary):
    q = PriorityQueue()
    for key in dictionary:
        q.put((dictionary[key], Node(key,dictionary[key])))
    return q

def generate_huffman_tree(q):
    tree = Tree()
    
    while q.qsize() > 3 :
        freq_left, node_left = q.get()
        freq_right, node_right = q.get()
        intermediate_node = Node(None, freq_left+freq_right)
        intermediate_node.set_left(node_left)
        intermediate_node.set_right(node_right)
        if q.qsize() == 2:
            freq_left, node_left = q.get()
            freq_right, node_right = q.get()
            intermediate_last_node = Node(None, freq_left+freq_right)
            intermediate_last_node.set_left(node_left)
            intermediate_last_node.set_right(node_right)
            root = Node(None, intermediate_node.frequency + intermediate_last_node.frequency)
            if intermediate_node < intermediate_last_node:
                root.set_left(intermediate_node)
                root.set_right(intermediate_last_node)
            else:
                root.set_left(intermediate_last_node)
                root.set_right(intermediate_node)
            tree.set_root(root)
            return tree

        q.put((intermediate_node.frequency, intermediate_node))

def huffman_encoding(data):
    dictionary = generate_dictionary(data)
    q = generate_priority_queue(dictionary)
    tree = generate_huffman_tree(q)
    print(tree.root.frequency)
    print(tree.root.left.frequency)
    print(tree.root.left.right.right.value)

def huffman_decoding(data,tree):
    pass

huffman_encoding("AAABBCCCCCCCCDE")
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