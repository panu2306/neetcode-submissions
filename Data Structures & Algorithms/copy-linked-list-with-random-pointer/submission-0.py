"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        The idea is to use two passes. In first pass, we can create a copy 
        of each node and store the value too. In second pass we will assign 
        the respective pointers. The reason we cannot do it one pass is 
        the random pointer which may point to the node which is not created 
        yet in the new linked list. Also, we need to use the hashmap to store 
        the new linked list and original linked where each item represents a mapping
        of original node to new node. 
        """

        # First pass - create a copy of original linked list and hashmap 
        curr = head 
        hashmap = {None: None}
        while curr: 
            new_node = Node(curr.val)
            hashmap[curr] = new_node
            curr = curr.next 
    
        # Second pass - assign pointers of new linked list - next and random 
        curr = head 
        while curr: 
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next 
        
        return hashmap[head]

             
            

        