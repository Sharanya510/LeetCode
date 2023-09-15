# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_sum, max_sum = 0,0
        queue = deque()
        queue.append(root)
        max_sum = root.val
        level, max_level = 1, 1
        while queue:
            size = len(queue)
            curr_sum = 0
            for i in range(size):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level=max(max_level,level)
            elif curr_sum==max_sum:
                max_sum=curr_sum
                max_level=min(max_level,level)
            level += 1
           
        return max_level
                    