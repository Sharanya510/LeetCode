# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        prev = dummy_node
        prev.next = head
        if (not head or not head.next) or left == right:
            return head
        left_pointer = self.GetPointerFromNode(prev, left)
        right_pointer = self.GetPointerFromNode(left_pointer.next, right - left)
        left_pointer.next = self.Reverse(left_pointer.next, right_pointer.next)
        return prev.next
    
    def GetPointerFromNode(self, start, val):
        count = 0
        while start.next and count < val - 1:
            start = start.next
            count +=1
        return start
    
    def Reverse(self, start, end):
        curr = start
        temp = start
        prev = end.next
        while prev != end:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
        return prev