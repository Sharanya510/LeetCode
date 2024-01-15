# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        # APPROACH --> RECURSION
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        # if not root:
        #     return None
        # temp = root.right 
        # root.right = root.left
        # root.left = temp
        # root.left = self.invertTree(root.left)
        # root.right = self.invertTree(root.right)
        # return root
        