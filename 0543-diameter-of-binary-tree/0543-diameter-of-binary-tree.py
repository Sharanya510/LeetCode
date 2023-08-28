# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.helper(root, self.max_diameter)
        return self.max_diameter
    
    def helper(self, root, max_diameter):
        if not root:
            return 0
        # nonlocal max_diameter
        left = self.helper(root.left, self.max_diameter)
        right = self.helper(root.right, self.max_diameter)
        self.max_diameter = max(self.max_diameter, left + right)
        return 1 + max(left, right)
        
        
        
        
        