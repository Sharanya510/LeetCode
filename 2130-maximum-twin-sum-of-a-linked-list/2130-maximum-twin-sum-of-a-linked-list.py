# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        values = []
        while temp:
            values.append(temp.val)
            temp = temp.next
        # print(values)
        i, j = 0, len(values) - 1
        max_sum = 0
        while i < j:
            max_sum = max(max_sum, values[i] + values[j])
            i += 1
            j -= 1
        return max_sum
        
            