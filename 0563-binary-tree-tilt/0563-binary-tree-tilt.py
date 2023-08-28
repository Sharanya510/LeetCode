# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.helper(root, self.total)
        return self.total
    
    def helper(self, root, total):
        if not root:
            return 0
        
        left = self.helper(root.left, self.total)
        right = self.helper(root.right, self.total)
        res = abs(left - right)
        self.total += res
        
        return left + right + root.val
        