# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # First method using set data structure: 
        # seen = set()
        # ptr = head 
        # while ptr: 
        #     if ptr in seen: 
        #         return True
        #     seen.add(ptr)
        #     ptr = ptr.next 
        # return False

        # second method using hare's cycle
        slow_ptr = head
        fast_ptr = head 

        while fast_ptr and fast_ptr.next: 
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next 
            if fast_ptr == slow_ptr:
                return True 
        return False

