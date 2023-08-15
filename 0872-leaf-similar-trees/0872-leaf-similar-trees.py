# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.res1 = []
        self.res2 = []
        self.helper(root1, self.res1)
        self.helper(root2, self.res2)
        return self.res1 == self.res2
    
    def helper(self, root, res):    
        if not root.left and not root.right:
            res.append(root.val)
        elif not root.left:
            self.helper(root.right, res)
        elif not root.right:
            self.helper(root.left, res)
        else:
            self.helper(root.left, res)
            self.helper(root.right, res)
        
        
        
        