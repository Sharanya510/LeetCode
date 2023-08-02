# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True
        
        
        #         RECURSIVE --- DEPTH FIRST SEARCH
#         min_val = float("-inf")
#         max_val = float("inf")
#         return self.helper(root, min_val, max_val)
        
#     def helper(self, root, min_val, max_val):
#         if not root:
#             return True
#         return root.val > min_val and root.val < max_val and self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
        