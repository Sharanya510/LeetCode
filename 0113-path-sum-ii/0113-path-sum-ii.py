# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res , temp = [], []
        self.helper(root, targetSum, res, temp)
        return res
    
    def helper(self, root, target, res, temp):
        if not root:
            return
        temp.append(root.val)
        if target == root.val and root.left is None and root.right is None:
            res.append(temp[:])
        
        target -= root.val
        self.helper(root.left, target, res, temp)
        self.helper(root.right, target, res, temp)
        temp.pop()
        return temp