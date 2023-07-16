# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        print(length)
        
        curr = head
        k = length - n
        if k == 0:
            return curr.next
        
        while k > 1:
            curr = curr.next
            k -= 1
        print(curr.val)
        
        if curr.next :
            curr.next = curr.next.next
            return head
        else:
            return None
            