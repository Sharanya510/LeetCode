# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head: return None
        dic = {}
        p = head
        while p:
            if p.val not in dic:
                dic[p.val] = 0
            dic[p.val] += 1
            p = p.next
        dummy = ListNode(0,head)
        slow = dummy
        curr = head
        while curr:
            if dic[curr.val] == 1:
                slow.next = curr
                slow = slow.next
            curr = curr.next
        slow.next = None    
        return dummy.next