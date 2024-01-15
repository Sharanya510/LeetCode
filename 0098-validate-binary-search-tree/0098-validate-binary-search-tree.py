# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        min_value = float("-inf")
        max_value = float("inf")
        
        my_stack = [(root, min_value, max_value)]
        while my_stack:
            root, lower, upper = my_stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            my_stack.append((root.left, lower, val))
            my_stack.append((root.right, val, upper))
        return True
    
        # APPROACH --> RECURSION
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXIXTY --> O(N)
#         min_value = float("-inf")
#         max_value = float("inf")
#         return self.helper(root, min_value, max_value)
    
#     def helper(self, root, min_val, max_val):
#         if not root:
#             return True
#         return (root.val > min_val and root.val < max_val and self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val , max_val))