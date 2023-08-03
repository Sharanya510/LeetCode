# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        curr_sum = 0
        h = defaultdict(int)
        self.helper(root, targetSum, h, curr_sum)
        return self.count
    
    def helper(self, root, target, h, curr_sum):
        if not root:
            return
        curr_sum += root.val
        
        if curr_sum == target:
            self.count += 1
        self.count += h[curr_sum - target]
        h[curr_sum] += 1
        self.helper(root.left, target, h, curr_sum)
        self.helper(root.right, target, h, curr_sum)
        h[curr_sum] -= 1
        
        
        