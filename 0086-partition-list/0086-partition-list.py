# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        before.next = after_head.next

        return before_head.next

        
        
        
# 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
                                   
# before --> 0 -> 3 -> 2 -> 1 ->
# after --> 0 -> 5 -> 8 -> 5 -> 10 ->
        