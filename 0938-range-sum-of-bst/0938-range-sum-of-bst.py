# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        output = 0
        self.helper(root,res)
        for i in range(len(res)):
            if res[i] >= low and res[i] <= high:
                output += res[i]
        return output
    def helper(self, root, res):
        if not root:
            return None
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
        