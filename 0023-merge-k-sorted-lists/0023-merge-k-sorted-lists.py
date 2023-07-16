# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        temp_list = []
        
        for c in lists:
            temp = c
            while temp:
                temp_list.append(temp.val)
                temp = temp.next
            
        temp_list.sort()
        
        dummy_node = ListNode(-1)
        print(temp_list)
        
        if temp_list:
            curr = ListNode(temp_list[0])

            dummy_node.next = curr
        
        for i in range(1, len(temp_list)):
            curr.next = ListNode(temp_list[i])
            curr = curr.next
        return dummy_node.next
        
        
        
            