# Union and Intersection of Two Linked List

Input: two linked list A and B </br>
Output: one linked list

Linked lists are used as input and output for this problem. A dictionary is created from the linked list A as an intermediate data structure for constant time lookup. Keys are elements in A and values are how many of that element in A (frequency).

## Algorithm for Union: 
1. Go through linked list A and generate dictionary (time complexity: O(n), space complexity: O(n))
2. Set new_linkedlist = linked list A
3. Go through linked list B (time complexity: O(n)). If this element is in A,
    * subtract frequency of this element in dictionary by one
    * if frequency becomes zero, delete this key from dictionary 
   If this element is not in A,
    * add this element to the new_linkedlist
4. Return new_linkedlist

## Algorithm for Intersection: 
1. Go through linked list A and generate dictionary (time complexity: O(n), space complexity: O(n))
2. Set new_linkedlist = None
3. Go through linked list B (time complexity: O(n). If this element is in A,
    * add this element to the new_linkedlist
    * subtract frequency of this element in dictionary by one
    * if frequency becomes zero, delete this key from dictionary 
4. Return new_linkedlist

## Overall Average Complexity:
The overall time and space complexity is O(n) for both Union and Intersection.