# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterative approach: 
        diameter = 0 
        if root is None: 
            return -1 
        

        
        stack = []
        node_depth_map = {}
        stack.append(root)

        while stack: 
            node = stack[-1]
            if node.left and node.left not in node_depth_map: 
                stack.append(node.left)
            elif node.right and node.right not in node_depth_map:
                stack.append(node.right)
            else: 
                stack.pop()
                left_height = node_depth_map.get(node.left, 0)
                right_height = node_depth_map.get(node.right, 0)
                node_depth_map[node] = 1 + max(left_height, right_height)
                diameter = max(diameter, left_height + right_height)
        return diameter

        