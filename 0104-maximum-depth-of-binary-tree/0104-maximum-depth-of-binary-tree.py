# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #APPROACH --> BFS
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right and not queue:
                return depth
            if node.left:
                queue.append([node.left, depth +1])
            if node.right:
                queue.append([node.right, depth +1])
        return depth
    
    
        #APPROACH --> RECURSION
        # TIME COMPLEXITY --> O(N)
        #  SPACE COMPLEXITY --> O(N)
        # if not root:
        #     return 0
        # left_height = self.maxDepth(root.left)
        # right_height = self.maxDepth(root.right)
        # return 1 + max(left_height, right_height)
        
        
        
        