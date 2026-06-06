# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        The idea is that we need to first find pairs and the length of list is even. The pairs 
        will be 0th element and (n-1)th element, 1st element and (n-2)th element.
        As we can see the last half part is reverse traversal. Therefore, we can divide
        the linked list into two halves and then reverse the second half. After that, we 
        can iterate to both and calculate sum of each pair and then return maxSum in the end. 
        """

        # find the mid, the next of mid would be start of second half 
        slow, fast = head, head.next

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
        
        first = head
        second = slow.next
        slow.next = None

        # reverse the second half 
        curr = second
        prev = None
        while curr: 
            temp = curr 
            curr = curr.next 
            temp.next = prev 
            prev = temp 
        second = prev 

        # iterate through two halves and calculate sum 
        max_sum = -1 
        curr_sum = -1
        
        while first:
            curr_sum = first.val + second.val 
            max_sum = max(curr_sum, max_sum)
            first = first.next 
            second = second.next
        return max_sum



        

        