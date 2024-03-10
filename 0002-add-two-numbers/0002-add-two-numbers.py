# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy_Head = ListNode(0)
        curr = Dummy_Head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            columnSum = l1_val + l2_val + carry
            carry = columnSum // 10
            nextNode = ListNode(columnSum % 10)
            curr.next = nextNode
            curr = nextNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return Dummy_Head.next