# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # APPROACH --> ONE PASS ALGORITHM
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
        p1 = head
        p2 = head
        if not head.next:
            return None
        while n:
            p1 = p1.next
            n -= 1
        if p1 is None:
            return p2.next
        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next
        if p2.next:
            p2.next = p2.next.next
        return head
        # APPROACH --> TWO PASS ALGO
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
#         temp = head
#         length = 0
#         while temp:
#             length += 1
#             temp = temp.next
        
#         curr = head
#         k = length - n
#         if k == 0:
#             return curr.next
#         while k > 1:
#             curr = curr.next
#             k -= 1
        
#         if curr.next:
#             curr.next = curr.next.next
#             return head
#         else:
#             return None