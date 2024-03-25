# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.largest = float('-inf')
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.largest
    
    def dfs(self,root):
        if not root:
            return 0
        
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)
   
        single_maximum = max(root.val,left_sum+root.val, right_sum+root.val)
        self.largest = max(self.largest,single_maximum,left_sum+right_sum+root.val)
        
        return single_maximum