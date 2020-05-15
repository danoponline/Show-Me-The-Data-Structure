import os

# Use Stack to hold directory path
class Stack:
    def __init__(self):
        self.arr = []
    
    def is_empty(self):
        return len(self.arr) == 0

    def push(self, value):
        self.arr.append(value)
        return

    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()

def find_files(suffix, path):
    if path is None or path == "" or not isinstance(path,str):
        print("Path has to be string type and cannot be None or empty")
        return

    stack = Stack()
    stack.push(path)
    list_of_paths_with_suffix = []

    # Worst-case time and space complexity are O(n) for n is a number of 
    # folders, subfolders, and files combined
    while not stack.is_empty():

        # Pop path at the top of the stack
        path = stack.pop()

        # Get the list of everything under this path
        list_of_stuff = os.listdir(path)
        
        # Loop through all the stuff. If directory found, push directory to stack.
        # If file found, append file ending with suffix into list_of_paths_with_suffix
        # Comment from mentor: use os.path.join to join the paths here
        for stuff in list_of_stuff:
            if os.path.isdir(path+ "/" + stuff):
                stack.push(path + "/" + stuff)
            elif os.path.isfile(path + "/" + stuff):
                if stuff.endswith(suffix):
                    list_of_paths_with_suffix.append(path + "/" + stuff)
            else:
                pass

    return list_of_paths_with_suffix

# Test case
print(find_files(".c", "./testdir"))
# Expected Output:
# ['./testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c']
print("--------------------------------------------------------------------")
print(find_files(".c", ""))
# Expected Outupt:
# Path has to be string type and cannot be None or empty
# None
print("--------------------------------------------------------------------")
print(find_files(".c", None))
# Expected Outupt:
# Path has to be string type and cannot be None or empty
# None