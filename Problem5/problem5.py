import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)
      self.next = None

    def calc_hash(self,data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
    
    def __repr__(self):
        s = "Timestamp: " + str(self.timestamp) + "\n"
        s += "Data: " + self.data + "\n"
        s += "Previous Hash: " + str(self.previous_hash) + "\n"
        s += "SHA256 Hash: " + str(self.hash) + "\n"
        s += "----------"
        return s

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def append(self,data):
        if data is None:
            print("Please provide a valid string data")
            return
        if self.is_empty():
            block_to_append = Block(datetime.datetime.utcnow(), data, 0)
            self.head = block_to_append
            self.tail = self.head
            return
        block_to_append = Block(datetime.datetime.utcnow(), data, self.tail.hash)
        self.tail.next = block_to_append
        self.tail = self.tail.next
        return

# Testing
print("Unit Test Start!")
print("-----------------------------------------------------------------------\n")

print("Test 1: Invalid input")
print("Expected Output: Please provide a valid string data)")
print("None")
print("Actual Output:", end=" ")
linkedlist = LinkedList()
linkedlist.append(None)
print(linkedlist.head)

print("\n-----------------------------------------------------------------------\n")

print("Test 2: Add one block")
print("Expected Output:", end="\n")
print("Timestamp: <current UTC time>")
print("Data: Block1")
print("Previous Hash: 0")
print("SHA256 Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("----------")
print("Actual Output:", end="\n")
linkedlist = LinkedList()
linkedlist.append("Block1")
print(linkedlist.head)

print("\n-----------------------------------------------------------------------\n")

print("Test 3: Add two blocks")
print("Expected Output:", end="\n")
print("Timestamp: <current UTC time>")
print("Data: Block1")
print("Previous Hash: 0")
print("SHA256 Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block2")
print("Previous Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("SHA256 Hash: 61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380")
print("----------")
print("Actual Output:", end="\n")
linkedlist.append("Block2")
print(linkedlist.head)
print(linkedlist.tail)

print("\n-----------------------------------------------------------------------\n")

print("Test 4: Add three blocks")
print("Expected Output:", end="\n")
print("Timestamp: <current UTC time>")
print("Data: Block1")
print("Previous Hash: 0")
print("SHA256 Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block2")
print("Previous Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("SHA256 Hash: 61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block3")
print("Previous Hash: 61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380")
print("SHA256 Hash: f76000270122d79ba262f8298080d37b8645d471d3885999274deba5caa7f704")
print("----------")
print("Actual Output:", end="\n")
linkedlist.append("Block3")
print(linkedlist.head)
print(linkedlist.head.next)
print(linkedlist.tail)

print("\n-----------------------------------------------------------------------\n")

print("Test 4: Add another block with a long name")
print("Expected Output:", end="\n")
print("Timestamp: <current UTC time>")
print("Data: Block1")
print("Previous Hash: 0")
print("SHA256 Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block2")
print("Previous Hash: 40e9b17a3391b5f461b2b96a2e5810a885f088346b901c65ebb5cf8cf7361103")
print("SHA256 Hash: 61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block3")
print("Previous Hash: 61edd5d6b03c20f764aab3bc4291b162ff48958e316603d4c07548a37872e380")
print("SHA256 Hash: f76000270122d79ba262f8298080d37b8645d471d3885999274deba5caa7f704")
print("----------")
print("Timestamp: <current UTC time>")
print("Data: Block has a longggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg name")
print("Previous Hash: f76000270122d79ba262f8298080d37b8645d471d3885999274deba5caa7f704")
print("SHA256 Hash: 213b8bb1c830ba6e12af06d53fe0bd68a0969c15392b6b05873e52dfb8d5f846")
print("----------")
print("Actual Output:", end="\n")
linkedlist.append("Block has a longggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg name")
print(linkedlist.head)
print(linkedlist.head.next)
print(linkedlist.head.next.next)
print(linkedlist.tail)

print("\n-----------------------------------------------------------------------\n")