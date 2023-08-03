# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return None
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right,res)
        
        
        # PRE-ORDER --> root, left, right
        # SINGLE LINE CODE
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []