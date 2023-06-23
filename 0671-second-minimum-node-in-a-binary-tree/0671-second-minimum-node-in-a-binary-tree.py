# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # USING A HELPER FUNCTION
        arr = sorted(set(self.TreeToList(root)))
        if len(arr) < 2 :
            return -1
        else:
            return arr[1]
        
    def TreeToList(self, root):
        if root is None:
            return []
        return self.TreeToList(root.left) + [root.val] + self.TreeToList(root.right)
        
        