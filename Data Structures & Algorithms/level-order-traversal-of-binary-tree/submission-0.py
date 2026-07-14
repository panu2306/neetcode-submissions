# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_queue = deque()
        res = []
        if root is None: 
            return res
        node_queue.append(root)
        while node_queue:
            node_queue_length = len(node_queue)
            level = []
            for node_index in range(node_queue_length): 
                curr = node_queue.popleft()
                level.append(curr.val)
                if curr.left: 
                    node_queue.append(curr.left)
                if curr.right:
                    node_queue.append(curr.right)
            res.append(level)
        return res
                
            
            
            
            
            
            

        