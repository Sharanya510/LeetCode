# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # APPROACH --> ITERATIVE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
        first_node = head
        mid_point = self.mid(first_node)
        second_head = self.reverse(mid_point.next)
        mid_point.next = None
        first_head = head
        Dummy_Node = ListNode(-1)
        Dummy_Node.next = first_head
        
        while second_head:
            next_first = first_head.next
            next_second = second_head.next
            first_head.next = second_head
            first_head = next_first
            second_head.next = first_head
            second_head = next_second
        return Dummy_Node.next
            
        
    def mid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        curr = head
        temp = head
        prev = None
        while curr:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
        return prev
        