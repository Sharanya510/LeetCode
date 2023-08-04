# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.helper(root, low, high)
        return self.res
    
    def helper(self, root, low, high):
        if not root:
            return
        if low <= root.val <= high:
            self.res += root.val
        self.helper(root.left, low, high)
        self.helper(root.right, low, high) 
        
# 10  5   15  3   7   n   18

    #     BRUTE -- FORCE
    #     res = []
    #     output = 0
    #     self.helper(root,res)
    #     for i in range(len(res)):
    #         if res[i] >= low and res[i] <= high:
    #             output += res[i]
    #     return output
    # def helper(self, root, res):
    #     if not root:
    #         return None
    #     self.helper(root.left,res)
    #     res.append(root.val)
    #     self.helper(root.right,res)
        