# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(-1)
        
        prev = dummy_head
        
        while l1 and l2:
            if l1.val <= l2.val :
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2
        
        return dummy_head.next
                
                
                
                
                
                
#   prev = dummy_head = -1              
# l1.  1 --> 2 --> 4
# l2.  1 --> 3 --> 4


        

        
        
        
        
        