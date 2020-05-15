# File Recursion

Please cd into this folder before running this program so that testdir can be properly found.

## Design Choices
Input: string suffix and string root path </br>
Output: list of all file paths with suffix

The file structure in this problem is similar to tree. Stack is used for this problem to store path for each node(directory) found along the traversal. Output is a list of file paths with user-specified suffix

## Algorithm

1. Initialize a stack
2. Push the root directory in the stack
3. In a while loop, 
    * pop the stack
    * check all files/directories
        * If directory found, add directory to stack
        * If file found, append file with user-specified suffix in a result list
4. Return the result list when the stack is empty

## Overall Complexity
The overall worst-case time and space complexity is O(n) where n is the total number of files, folders, and subfolders combined. The while loop in the algorithm takes the longest time to complete