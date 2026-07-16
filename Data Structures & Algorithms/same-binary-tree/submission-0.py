# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _dfs(p, q):
            if p is None and q is None: 
                return True
            if p is None or q is None or p.val != q.val: 
                return False
            return (_dfs(p.left, q.left) and _dfs(p.right, q.right))
        return _dfs(p, q)