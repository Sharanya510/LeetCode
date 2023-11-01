# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.count = 0
        return self.helper(root) + 1
    
    def helper(self, root):
        if not root:
            return 0
        if root.left:
            self.count += 1
            self.helper(root.left)
        if root.right:
            self.count += 1
            self.helper(root.right)
        return self.count
        
        
        
        
#         if root.left:
#             self.count += 1
#             self.countNodes(root.left)
            
#         if root.right:
#             self.count += 1
#             self.countNodes(root.right)
#         return self.count +1 
            
        