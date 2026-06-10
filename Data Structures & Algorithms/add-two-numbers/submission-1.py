# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy 
        carry = 0 
        while l1 and l2: 
            curr_sum = l1.val + l2.val + carry
            carry = curr_sum // 10 
            digit = curr_sum % 10 
            result.next = ListNode(digit)
            l1 = l1.next
            l2 = l2.next
            result = result.next
        while l1: 
            curr_sum = l1.val + carry
            carry = curr_sum // 10 
            digit = curr_sum % 10 
            result.next = ListNode(digit)
            l1 = l1.next
            result = result.next
        while l2: 
            curr_sum = l2.val + carry
            carry = curr_sum // 10 
            digit = curr_sum % 10 
            result.next = ListNode(digit)
            l2 = l2.next  
            result = result.next
        if carry: 
            
            result.next = ListNode(carry)
            result = result.next
        return dummy.next

        