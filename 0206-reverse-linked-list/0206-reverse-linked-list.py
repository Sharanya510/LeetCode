# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # APPROACH 2 --> RECURSIVE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        if (not head) or (not head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        
        # APPROACH 1 --> ITERATIVE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
        # curr = head
        # temp = head
        # prev = None
        # while curr:
        #     curr = curr.next
        #     temp.next = prev
        #     prev = temp
        #     temp = curr
        # return prev