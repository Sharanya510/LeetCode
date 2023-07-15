# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         first_node = head
#         mid = self.midpoint(first_node)
#         second_head = self.reverse(mid)
#         first_head = head
#         dummy_node = ListNode(-1)
#         dummy_node.next = head

#         while second_head.next:
#             print("hi")
#             first_head.next = second_head
#             first_head = first_head.next
#             second_head.next = first_head
#             second_head = second_head.next
            
 
    
#     def midpoint(self, head):
#         slow = head
#         fast = head
#         while fast.next and fast.next.next :
#             slow = slow.next
#             fast = fast.next.next
#         # slow.next = None
#         return fast

#     def reverse(self, head):
#         prev = None
#         curr = head
#         temp = head

#         while curr:
#             curr = curr.next
#             temp.next = prev
#             prev = temp
#             temp = curr
#         return prev
        
       # prev = dummy_node
        
        #  1 2 3 4 
            
#   -1     1 2 3  4
#          4 3->none
#          1 4  

        # return dummy_node
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        first_node = head
        mid = self.midpoint(first_node)
        second_head = self.reverse(mid.next)
        mid.next = None
        first_head = head

        while second_head:
            next_first = first_head.next
            next_second = second_head.next
            first_head.next = second_head
            second_head.next = next_first
            first_head = next_first
            second_head = next_second

    def midpoint(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

            
            
        
        