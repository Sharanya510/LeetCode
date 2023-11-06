# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        prev=dummy
        prev.next=head
        if not (head and head.next) or left==right: return head
        leftpointer=self.getpointerbeforenode(prev, left)
        rightpointer=self.getpointerbeforenode(leftpointer.next,right-left)
        leftpointer.next=self.reverse(leftpointer.next,rightpointer.next)
        return prev.next
 
    def getpointerbeforenode(self,start,val):
        count=0
        while start.next and count<val-1:
            start=start.next
            count+=1
        return start
    
    def reverse(self,start,end):
        prev=end.next
        curr=start
        temp=start
        while prev!=end:
            curr = curr.next
            temp.next = prev
            prev = temp
            temp = curr
        return prev
        