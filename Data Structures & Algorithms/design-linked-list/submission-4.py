# class ListNode:
#     def __init__(self, val: int):
#         self.val = val
#         self.next = None
        
# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.length: 
#             return -1 
#         curr = self.head 
#         for _ in range(index):
#             curr = curr.next
#         return curr.val 
        

#     def addAtHead(self, val: int) -> None:
#         new_node = ListNode(val)
#         if self.length == 0: 
#             self.head = new_node
#             self.tail = self.head
#         else:
#             new_node.next = self.head
#             self.head = new_node   
#         self.length += 1 
        

#     def addAtTail(self, val: int) -> None:
#         new_node = ListNode(val)
#         if self.length == 0: 
#             self.head = new_node
#             self.tail = self.head
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index >= self.length: 
#             return 
#         if index == 0:
#             self.addAtHead(val)
#             return
#         if index == self.length - 1:
#             self.addAtTail(val)
#             return
    
#         new_node = ListNode(val)
#         curr = self.head 
#         for _ in range(index - 1): 
#             curr = curr.next
#         new_node.next = curr.next            
#         curr.next = new_node
#         self.length += 1 
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.length:
#             return
#         if index == 0: 
#             curr = self.head 
#             self.head = self.head.next 
#             if self.length == 1: 
#                 self.tail = None
#             self.length -= 1 
#             return
        
#         curr = self.head 
#         for _ in range(index - 1): 
#             curr = curr.next 
#         if index == self.length - 1:
#             self.tail = curr
#         curr.next = curr.next.next
#         self.length -= 1
         
            
                
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.length:
            return -1

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val: int) -> None:

        node = ListNode(val)

        node.next = self.head
        self.head = node

        if self.length == 0:
            self.tail = node

        self.length += 1

    def addAtTail(self, val: int) -> None:

        node = ListNode(val)

        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        temp = self.head

        
        for _ in range(index - 1):
            temp = temp.next

        node = ListNode(val)

        node.next = temp.next
        temp.next = node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.length:
            return

        if index == 0:

            self.head = self.head.next

            if self.length == 1:
                self.tail = None

            self.length -= 1
            return

        temp = self.head

        for _ in range(index - 1):
            temp = temp.next

        if index == self.length - 1:
            self.tail = temp

        temp.next = temp.next.next

        self.length -= 1


        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)