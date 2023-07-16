# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_list = []
        temp = head
        while temp:
            temp_list.append(temp.val)
            temp = temp.next
        
        n = len(temp_list)
        
        temp_list[k-1], temp_list[n-k] = temp_list[n-k], temp_list[k-1]
        
        dummy_node = ListNode(-1)
        
        curr = ListNode(temp_list[0])
        
        dummy_node.next = curr
        
        for i in range(1, len(temp_list)):
            curr.next = ListNode(temp_list[i])
            curr = curr.next
            
        return dummy_node.next