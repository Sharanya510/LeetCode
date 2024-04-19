# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first_node=head
        second_node=head.next
        prev=ListNode(-1)
        dummy=prev
        
        while head and head.next:
            first_node=head
            second_node=head.next
            prev.next=second_node
            first_node.next=second_node.next
            second_node.next=first_node
            prev=head
            head=first_node.next
        return dummy.next
    
            
  
#             p
#             |
# #         1 2 3 4 5 6
# #     d   f
# #           s
        
# #      -2-1->3-4
# #       s f  
#              h
#           p
# #     d 
    
# #        2-1-4-3-5-6
# #                f s
# #                p
    
    
    
    
    
    
    
    
    
    
  
             