# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    
# from typing import List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.solution = []

    def get_height(self, root: TreeNode) -> int:
        # return -1 for null nodes
        if root is None:
            return -1
        
        # first calculate the height of the left and right children
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        # calculate the current node's height
        curr_height = max(left_height, right_height) + 1
        
        # if the solution list is not big enough, add a new list for the current height
        if len(self.solution) == curr_height:
            self.solution.append([])
        
        # add the current node's value to the corresponding height list
        self.solution[curr_height].append(root.val)
        
        return curr_height

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.solution = []
        
        self.get_height(root)
        
        return self.solution

        