# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.helper(root, 0, res)
        return res
    
    def helper(self, node, level, res):
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.helper(node.left, level + 1, res)
        if node.right:
            self.helper(node.right, level + 1, res)
        
        # APPROACH --> ITERATIVE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        # if not root:
        #     return None
        # queue = deque()
        # queue.append(root)
        # res = []
        # while queue:
        #     temp = []
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         temp.append(node.val)
        #     res.append(temp)
        # return res