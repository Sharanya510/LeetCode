# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        heap = []
        
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        # print(heap)
        dummy_node = ListNode(-1)
        
        curr = dummy_node
        
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
            # print(heap)
        return dummy_node.next
        