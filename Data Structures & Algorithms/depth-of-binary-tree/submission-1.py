# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth-first search solution: 
        if root is None: 
            return 0 

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # Iterative BFS solution: 
        # if root is None: 
        #     return 0 
        # node_queue = deque()
        # node_queue.append(root) 
        # levels = 0 

        # while node_queue:
        #     for node_index in range(len(node_queue)): 
        #         curr_node = node_queue.popleft()
        #         if curr_node.left: 
        #             node_queue.append(curr_node.left)
        #         if curr_node.right: 
        #             node_queue.append(curr_node.right) 
        #     levels += 1 
        # return levels
   