# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        first_half_end = self.finding_midpoint(head)
        second_half_start = self.reverse(first_half_end.next)
        
        first_position = head
        second_position = second_half_start
        while second_position:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next
        return True
            
    def finding_midpoint(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow. next
        return slow
    def reverse(self, head):
        prev = None
        temp = head
        curr = head
        while temp:
            temp = temp.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
        
        
        
        
        
        
        
        
        # BRUTE-FORCE
        # temp1 = head
        # list1 = []
        # while temp1:
        #     list1.append(temp1.val)
        #     temp1 = temp1.next
        # return list1 == list1[::-1]
        