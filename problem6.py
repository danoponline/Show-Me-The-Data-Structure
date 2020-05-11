class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self,value):
        # Get new node ready to prepend
        new_node = Node(value)
        
        # For empty node
        if self.is_empty():
            self.head = new_node
            self.size += 1
            return
        
        # For node that already have elements
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def is_empty(self):
        return self.size == 0

    # (For testing only) Print the linked list 
    def print_LinkedList(self):
        if self.is_empty():
            print("Nothing to print. Linked list is empty!")
            return 
        print("[Head:", end=" ")
        node = self.head
        while (node is not None):
            if node.next is not None:
                print("(" + format(node.value) + ")", end="->")
            else:
                print("(" + format(node.value) + ")", end=" :Tail]\n")
            node = node.next

def intersection(linkedlist1, linkedlist2):
    pass

def union(linkedlist1, linkedlist2):
    pass

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.prepend(i)

for i in element_2:
    linked_list_2.prepend(i)