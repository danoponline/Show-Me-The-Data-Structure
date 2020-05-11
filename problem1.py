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

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(2, 2)
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(3, 3)
our_cache.set(3, 3)
our_cache.set(2, 2)
our_cache.set(4, 4)
our_cache.set(4, 4)
our_cache.set(2, 2)
our_cache.set(5, 5)

print("Return value from get: " + format(our_cache.get(3)))
print("Return value from get: " + format(our_cache.get(5)))
print("Return value from get: " + format(our_cache.get(1)))
our_cache.set(0,0)
print(our_cache.head.value)
print(our_cache.head.next.value)
print(our_cache.head.next.next.value)
print(our_cache.head.next.next.next.value)
print(our_cache.head.next.next.next.next.value)

# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5) 
# our_cache.set(6, 6)

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
