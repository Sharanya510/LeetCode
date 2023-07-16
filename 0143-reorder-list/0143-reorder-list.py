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
        
        first_node = head
        mid = self.midpoint(first_node)
        #print(mid.val)
        second_head = self.reverse(mid.next)
        #print(second_head.val)
        mid.next = None
        first_head = head
        dummy_node = ListNode(-1)
        dummy_node.next = first_head

        while second_head:
            next_first=first_head.next
            next_second=second_head.next
            first_head.next = second_head
            first_head = next_first
            second_head.next = first_head
            second_head = next_second
        return dummy_node.next          
  #  1 2 3 4 
            
#   -1     1 2->none 
#          4 3->none

# 1->4->2->3->none

#          1 4  
    
    def midpoint(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        curr = head
        temp = head

        while curr:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
        return prev
            
        
            
            
        
        