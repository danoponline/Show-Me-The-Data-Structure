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

# Overall Time complexity for this function is O(n)
def intersection(linkedlist1, linkedlist2):
    
    # Time complexity is O(n) to generate this dictionary
    dict_1 = generate_dictionary(linkedlist1)
    new_linkedlist = LinkedList()
    node_in_ll2 = linkedlist2.head
    
    # Time complexity is O(n) to loop through this linked list
    while node_in_ll2 is not None:
        # Time complexity is O(1) to look up dictionary
        if node_in_ll2.value in dict_1:
            # Time complexity is O(1) to prepend a new node
            new_linkedlist.prepend(node_in_ll2.value)
            dict_1[node_in_ll2.value] -= 1
            if dict_1[node_in_ll2.value] == 0:
                del dict_1[node_in_ll2.value]
        node_in_ll2 = node_in_ll2.next
    return new_linkedlist

# Overall Time complexity for this function is O(n)
def union(linkedlist1, linkedlist2):
    # Time complexity is O(n) to generate this dictionary
    dict_1 = generate_dictionary(linkedlist1)
    new_linkedlist = linkedlist1
    node_in_ll2 = linkedlist2.head
    
    # Time complexity is O(n) to loop through this linked list
    while node_in_ll2 is not None:
        # Time complexity is O(1) to look up dictionary
        if node_in_ll2.value in dict_1:
            
            dict_1[node_in_ll2.value] -= 1
            if dict_1[node_in_ll2.value] == 0:
                del dict_1[node_in_ll2.value]
        
        else:
            # Time complexity is O(1) to prepend a new node
            new_linkedlist.prepend(node_in_ll2.value)
        
        node_in_ll2 = node_in_ll2.next
    return new_linkedlist

# Function to generate dictionary for look up
# Time complexity is O(n)
def generate_dictionary(linkedlist):
    
    # This dictionary contain {value1 : frequency1,...} 
    # for constant time look up
    dictionary = {}
    current_node = linkedlist.head

    # Loop through all nodes
    while current_node is not None:
        # if not yet in dictionary, add it with frequency=1
        if current_node.value not in dictionary:
            dictionary[current_node.value] = 1
        # if already in dictionary, add frequency by 1
        else:
            dictionary[current_node.value] += 1
        current_node = current_node.next

    return dictionary

# Generate Linked List from Python list (for testing only)
def generate_linkedlist(python_list):
    linked_list = LinkedList()
    for i in python_list:
        linked_list.prepend(i)
    return linked_list

# Unit Test
print("Unit Test Start!")
print("-----------------------------------------------------------------------")
print("Test 1: Empty linked list (list1 = list2 = [])")
print("-----------------------------------------------------------------------")
list1 = []
list2 = []
linked_list1 = generate_linkedlist(list1)
linked_list2 = generate_linkedlist(list2)
result_intersection = intersection(linked_list1,linked_list2)
result_union = union(linked_list1,linked_list2)

print("Intersection Test")
print("Expected Linked List: Nothing to print. Linked list is empty!")
print("Actual Linked List:", end=" ")
result_intersection.print_LinkedList()
print("", end="\n")
print("Union Test")
print("Expected Linked List: Nothing to print. Linked list is empty!")
print("Actual Linked List:", end=" ")
result_union.print_LinkedList()

print("\n-----------------------------------------------------------------------")

print("Test 2: Repeated elements")
print("        list1 = [1,1,1], list2 = [1]")
print("-----------------------------------------------------------------------")
list1 = [1,1,1]
list2 = [1]
linked_list1 = generate_linkedlist(list1)
linked_list2 = generate_linkedlist(list2)
result_intersection = intersection(linked_list1,linked_list2)
result_union = union(linked_list1,linked_list2)

print("Intersection Test")
print("Expected Linked List: [Head: (1) :Tail]")
print("Actual Linked List:", end=" ")
result_intersection.print_LinkedList()
print("", end="\n")
print("Union Test")
print("Expected Linked List: [Head: (1)->(1)->(1) :Tail]")
print("Actual Linked List:", end=" ")
result_union.print_LinkedList()

print("\n-----------------------------------------------------------------------")

print("Test 3: None elements")
print("        list1 = [1,1,None], list2 = [None]")
print("-----------------------------------------------------------------------")
list1 = [1,1,None]
list2 = [None]
linked_list1 = generate_linkedlist(list1)
linked_list2 = generate_linkedlist(list2)
result_intersection = intersection(linked_list1,linked_list2)
result_union = union(linked_list1,linked_list2)

print("Intersection Test")
print("Expected Linked List: [Head: (None) :Tail]")
print("Actual Linked List:", end=" ")
result_intersection.print_LinkedList()
print("", end="\n")
print("Union Test")
print("Expected Linked List: [Head: (None)->(1)->(1) :Tail]")
print("Actual Linked List:", end=" ")
result_union.print_LinkedList()

print("\n-----------------------------------------------------------------------")

print("Test 4: Test case from problem statement")
print("        list1 = [3,2,4,35,6,65,6,4,3,21]")
print("        list2 = [6,32,4,9,6,1,11,21,1]")
print("-----------------------------------------------------------------------")
list1 = [3,2,4,35,6,65,6,4,3,21]
list2 = [6,32,4,9,6,1,11,21,1]
linked_list1 = generate_linkedlist(list1)
linked_list2 = generate_linkedlist(list2)
result_intersection = intersection(linked_list1,linked_list2)
result_union = union(linked_list1,linked_list2)

print("Intersection Test")
print("Expected Linked List: [Head: (6)->(4)->(6)->(21) :Tail]")
print("Actual Linked List:", end=" ")
result_intersection.print_LinkedList()
print("", end="\n")
print("Union Test")
print("Expected Linked List: [Head: (32)->(9)->(1)->(11)->(1)->(21)->(3)->(4)->(6)->(65)->(6)->(35)->(4)->(2)->(3) :Tail]")
print("Actual Linked List:", end=" ")
result_union.print_LinkedList()

print("\n-----------------------------------------------------------------------")

print("Test 5: Test case from problem statement")
print("        list1 = [3,2,4,35,6,65,6,4,3,23]")
print("        list2 = [1,7,8,9,11,21,1]")
print("-----------------------------------------------------------------------")
list1 = [3,2,4,35,6,65,6,4,3,23]
list2 = [1,7,8,9,11,21,1]
linked_list1 = generate_linkedlist(list1)
linked_list2 = generate_linkedlist(list2)
result_intersection = intersection(linked_list1,linked_list2)
result_union = union(linked_list1,linked_list2)

print("Intersection Test")
print("Expected Linked List: Nothing to print. Linked list is empty!")
print("Actual Linked List:", end=" ")
result_intersection.print_LinkedList()
print("", end="\n")
print("Union Test")
print("Expected Linked List: [Head: (1)->(7)->(8)->(9)->(11)->(21)->(1)->(23)->(3)->(4)->(6)->(65)->(6)->(35)->(4)->(2)->(3) :Tail]")
print("Actual Linked List:", end=" ")
result_union.print_LinkedList()

print("\n-----------------------------------------------------------------------")