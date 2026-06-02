class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) 
    
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0: 
            curr = curr.next 
            index -= 1 
        return curr.val if curr and index == 0 else -1 
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head.next is None:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head
        while curr.next: 
            curr = curr.next 
        curr.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head 
        while curr and index > 0: 
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new_node.next = curr.next
            curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        while curr.next and index > 0: 
            curr = curr.next
            index -= 1
        if curr.next and index == 0:
            temp = curr.next
            curr.next = temp.next
            temp.next = None 
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)