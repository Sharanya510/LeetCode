# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         BFS
# QUEUE
        if not root:
            return None
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            temp = []
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
                # print(temp)
            res.append(temp)
            # print(res)
        return res
            