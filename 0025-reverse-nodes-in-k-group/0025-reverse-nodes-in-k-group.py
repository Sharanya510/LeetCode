# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self, head, k):
        curr = head
        temp = head
        prev = None
        while k:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
            k -= 1
        return prev
    def reverseKGroup(self, head, k):
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        if count == k:
            reversedHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
        
#         1 2 3 4 5 6 7 8 9
#         h                 
#               p
#               3
        
# reversedHead=reverselinkedlist(1->2->3)
               

#          3-2-1-6->5->4->9->8->7-none

#             reversedHead=reverselinkedlist(4->5->6)
#                                 6->5->4->9->8->7-none
#                            reversedHEAD=reve.rselinkedlist(7->8->9)
#                                     9->8->7-none
                        
                        
#           1 2 3
#           p
        
#             newhead=none
#             ptr=head=1
#             next_node=