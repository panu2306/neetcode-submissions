# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def _dfs(root):
            if root is None:
                return result
            result.append(root.val)
            _dfs(root.left)
            _dfs(root.right)
        _dfs(root)
        return result
        