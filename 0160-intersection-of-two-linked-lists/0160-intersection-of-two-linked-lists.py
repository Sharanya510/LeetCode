# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        posA = headA
        posB = headB
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        if (lenA - lenB > 0):
            while( lenA != lenB):
                posA = posA.next
                lenA -= 1               
        elif (lenB - lenA > 0): 
            while(  lenB != lenA):
                posB = posB.next
                lenB -= 1
        
        while(posA != posB):
            posA = posA.next
            posB = posB.next
        return posA
        
    def getLen(self,headA):
        if (headA == None):
            return 0
        len = 0
        while (headA) :
            len += 1
            headA = headA.next
        return len
    
        # while temp1 != temp2:
        #     if temp1 is not None:
        #         temp1 = temp1.next
        #     else:
        #         temp1 = headB
        #     if temp2 is not None:
        #         temp2 = temp2.next
        #     else:
        #         temp2 = headA
        # return temp1
        
        
                
        