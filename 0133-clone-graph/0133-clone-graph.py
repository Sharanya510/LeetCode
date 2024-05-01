"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned={}
        queue=deque()
        queue.append(node)
        cloned[node]=Node(node.val,[])
        while queue:
            n=queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor]=Node(neighbor.val,[])
                    queue.append(neighbor)
                cloned[n].neighbors.append(cloned[neighbor])
                
        return cloned[node]
                
                
        