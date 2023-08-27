# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        list1 = []
        while temp1:
            list1.append(temp1.val)
            temp1 = temp1.next
        # print(list1)
        return list1 == list1[::-1]
            
            
            
            
        # prev = None
        # temp = head
        # curr = head
        # while temp:
        #     temp = temp.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # prev = head
        # while prev:
        #     list2.append(prev.val)
        #     prev = prev.next
        # print(list1)
        # print(list2)
        # return list1 == list2
        
        
            
        
        
        
        
        
# None    1   2   2   1
# prev    t
#         c
#         p   t