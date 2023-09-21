# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        second_head = self.reverse(fast)
        first_head = head
        max_sum = 0
        
        while second_head:
            max_sum = max(max_sum, first_head.val + second_head.val)
            first_head = first_head.next
            second_head = second_head.next
        return max_sum
    
    def reverse(self, head):
        prev = None
        temp = head
        curr = head
        while temp:
            curr=curr.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev       
        
        
        # BRUTE-FORCE
        # temp = head
        # new_list = []
        # while temp:
        #     new_list.append(temp.val)
        #     temp = temp.next
        # # print(new_list)
        # i, j = 0, len(new_list) - 1
        # max_sum = 0
        # while i < j:
        #     max_sum = max(max_sum, new_list[i] + new_list[j])
        #     i += 1
        #     j -= 1
        # return max_sum