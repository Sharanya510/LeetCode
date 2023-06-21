# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DEPTH --- FIRST --- SEARCH
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        
        
        
        
        
        
        
        
        
        
#  -------- BRUTE--- FORCE -------
#         length = 0
#         res_left, res_right = 1, 1
#         if not root:
#             return length
        
#         if root.left:
#             res_left += 1
#         self.maxDepth(root.left)
#         self.maxDepth(root.right)
        
#         if root.right:
#             res_right += 1
#         self.maxDepth(root.left)
#         self.maxDepth(root.right)
        
#         length = 1 + max(res_left,res_right )
#         return length
        
        