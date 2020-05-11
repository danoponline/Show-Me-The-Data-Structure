class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache:

    def __init__(self, capacity):
        # Use dictionary with some key and value as node in doubly linked list
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent (cache miss)
        if key not in self.cache:
            return -1
        
        # cache hit
        cache_hit_node = self.cache[key]
        self._move_to_tail(cache_hit_node)
        return cache_hit_node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.is_empty():
            self.cache[key] = Node(key,value)
            self.head = self.cache[key]
            self.tail = self.head
            return

        if key not in self.cache:

            if self.is_full():
                self._remove_head()

            # Setup new node with key : Node(key,value) pair
            self.cache[key] = Node(key,value) 
            this_node = self.cache[key]

            # Add this_node to tail
            self._add_to_tail(this_node)

            return
        
        else:
            # This key already exists in the cache. We need to move the key to the tail
            this_node = self.cache[key]
            
            # Reset this node to have the new value
            this_node.value = value

            # Move this_node to tail
            self._move_to_tail(this_node)


    def is_empty(self):
        return len(self.cache) == 0

    def is_full(self):
        return len(self.cache) == self.capacity

    # Private use in case the cache is full
    def _remove_head(self):
        
        # Setup the node next to the old head to be the new head
        self.head = self.head.next
        new_head = self.head
        old_head = new_head.previous
        
        # Remove the old head key from the dictionary
        del self.cache[old_head.key]

        # Complete detach the old head from the linked list
        old_head.key = None
        old_head.value = None
        old_head.next = None
        old_head.previous = None
        new_head.previous = None
        return

    # Private use to move this node to tail
    def _move_to_tail(self, this_node):
        
        # Do nothing if this_node is already the tail
        if this_node == self.tail:
            return

        # Need to reset head if this_node is the head
        if this_node == self.head:
            # Set the next node to the old head to be the new head
            self.head = self.head.next
            self.head.previous = None
            
            # Add this_node to tail
            self._add_to_tail(this_node)
            return

        # Detach this_node and reconnect wires
        this_node.previous.next = this_node.next
        this_node.next.previous = this_node.previous
        
        # Add this_node to tail
        self._add_to_tail(this_node)
        return

    # Private use to add this node to tail
    def _add_to_tail(self, this_node):
        
        # Setup this new node previous to the old tail and next to be None
        this_node.previous = self.tail
        this_node.next = None

        # Setup the old tail next to be this node
        self.tail.next = this_node

        # Setup this node to be the current tail
        self.tail = this_node
        return

    # (For testing only) Print the linked list 
    def print_cache(self):
        if self.is_empty():
            print("Nothing to print. Cache is empty!")
            return 
        print("[Head:", end=" ")
        node = self.head
        while (node is not None):
            if node.next is not None:
                print("(" + format(node.key) + "," + format(node.value) + ")", end="->")
            else:
                print("(" + format(node.key) + "," + format(node.value) + ")", end=" :Tail]\n")
            node = node.next

# Unit Test
print("Unit Test Start!")
print("-----------------------------------------------------------------------\n")

print("Test 1: Print empty cache")
our_cache = LRU_Cache(5)
print("Expected Linked List: Nothing to print. Cache is empty!")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 2: Set cache with (key=1,value=1) element")
our_cache.set(1, 1)
print("Expected Linked List: [Head: (1,1) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 3: Set cache with (key=2,value=2) element")
our_cache.set(2, 2)
print("Expected Linked List: [Head: (1,1)->(2,2) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 4: Set cache with (key=1,value=1) element (key already in cache)")
our_cache.set(1, 1)
print("Expected Linked List: [Head: (2,2)->(1,1) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 5: Get cache with (key=2) element (key already in cache)")
print("Expected value: 2")
print("Actual value: " + format(our_cache.get(2)))
print("Expected Linked List: [Head: (1,1)->(2,2) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 6: Get cache with (key=5) element (key NOT in cache)")
print("Expected value: -1")
print("Output value: " + format(our_cache.get(5)))
print("Expected Linked List: [Head: (1,1)->(2,2) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 7: Set cache full with key and value from 1 to 5")
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
print("Expected Linked List: [Head: (1,1)->(2,2)->(3,3)->(4,4)->(5,5) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 8: Get cache with (key=3) element (key already in cache)")
print("Expected value: 3")
print("Output value: " + format(our_cache.get(3)))
print("Expected Linked List: [Head: (1,1)->(2,2)->(4,4)->(5,5)->(3,3) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 9: Get cache with (key=1) element (key is the head in cache)")
print("Expected value: 1")
print("Output value: " + format(our_cache.get(1)))
print("Expected Linked List: [Head: ((2,2)->(4,4)->(5,5)->(3,3)->(1,1) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 10: Set cache with (key=6,value=6) element (key NOT in cache)")
our_cache.set(6, 6)
print("Expected Linked List: [Head: ((4,4)->(5,5)->(3,3)->(1,1)->(6,6) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 11: Get cache with (key=2) element (key NOT in cache)")
print("Expected value: -1")
print("Output value: " + format(our_cache.get(2)))
print("Expected Linked List: [Head: ((4,4)->(5,5)->(3,3)->(1,1)->(6,6) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------\n")

print("Test 12: Set cache with (key=5,value=10) element (key already in cache)")
our_cache.set(5, 10)
print("Expected Linked List: [Head: ((4,4)->(3,3)->(1,1)->(6,6)->(5,10) :Tail]")
print("Actual Linked List:", end=" ")
our_cache.print_cache()

print("\n-----------------------------------------------------------------------")
print("Unit Test Complete!")