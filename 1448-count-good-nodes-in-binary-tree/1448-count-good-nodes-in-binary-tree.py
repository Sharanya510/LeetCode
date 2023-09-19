# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_good_nodes = 0
        self.max_so_far = float("-inf")
        self.helper(root, self.num_good_nodes, self.max_so_far)
        return self.num_good_nodes
        
        
    def helper(self, root, num_good_nodes, max_so_far):
        if root.val >= max_so_far:
            self.max_so_far = root.val
            self.num_good_nodes += 1
        if root.left:
            self.helper(root.left, num_good_nodes, max(root.val, max_so_far))
        if root.right:
            self.helper(root.right, num_good_nodes, max(root.val, max_so_far))
        
        