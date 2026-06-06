# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # count length of LL 
        # get mid 
        # divide first half in same order 
        # divide second half in reverse order -> reverse a LL 
        # join two lists 
        curr = head 
        length = 0
        while curr: 
            curr = curr.next 
            length += 1 
        
        len_second_half = length // 2 
        len_first_half = length - len_second_half

        curr = head 
        ptr1 = head 
        count = 0
      

        while curr: 
            if count == len_first_half - 1: 
                tail = curr
                ptr2 = tail.next
                tail.next = None
            count += 1
            curr = curr.next 
        
        # reverse second half: 
        prev, curr = None, ptr2 
        while curr: 
            temp = curr
            curr = curr.next 
            temp.next = prev
            prev = temp 
        ptr2 = prev 

        # join two lists - ptr1 and ptr2 

        head = ptr1 
        
 
        while ptr2: 
            n1 = ptr1.next
            n2 = ptr2.next 
            ptr1.next = ptr2 
            ptr2.next = n1 
            ptr1 = n1
            ptr2 = n2
    
            
        


       

        

        

            
        
    
        