# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root: return None
        if root.left:
            self.helper(root.left, res)
        if root:
            res.append(root.val)
        if root.right:
            self.helper(root.right, res)
        return res
        