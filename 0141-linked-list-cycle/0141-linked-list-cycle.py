# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # APPROACH --> HAASH TABLE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        nodes_seen = set()
        while head:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
    
        # APPROACH --> FLOYD'S CYCLE FINDING ALGORITHM
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
        # if not head:
        #     return False
        # slow = head
        # fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False