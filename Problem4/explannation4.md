# Active Directory

Input: string user_input and Group group_input </br>
Output: boolean if user_input is within group_input

The group structure in this problem is similar to tree. Stack is used for this problem to store child group within each parent group found along the traversal.

## Algorithm

1. Check if users provide valid input. Otherwise, return False
2. Initialize a stack
3. Push the group_input in the stack
4. In a while loop, 
    * pop the stack
    * check users in this group
        * If user found, return True
    * add subgroups within this group into the stack
4. Return False if user is not found

The overall worst-case time and space complexity is O(n) where n is the total number of groups. The while loop in the algorithm takes the longest time to complete.