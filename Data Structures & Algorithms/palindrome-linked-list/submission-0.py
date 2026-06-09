# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        The idea is to find mid using slow, fast pointers. After finding mid, reverse the 
        linked list starting after mid. Then we can compare both if all values of each nodes 
        are equal if number of nodes are even and all but on equal if number of nodes are odd. 
        """
        dummy = ListNode(0, head)
        slow, fast = dummy, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        mid = slow.next 
        slow.next = None

        prev = None 
        
        while mid: 
            temp = mid.next 
            mid.next = prev
            prev = mid 
            mid = temp
        
        first = head
        second = prev 

        while first: 
            if first.val != second.val: 
                return False 
            first = first.next
            second = second.next
        
        return False if second and second.next else True
             

         



        