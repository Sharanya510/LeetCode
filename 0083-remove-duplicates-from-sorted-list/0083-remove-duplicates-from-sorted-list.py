# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
#         temp = head
#         temp_list = []
#         while temp:
#             temp_list.append(temp.val)
#             temp = temp.next
#         print(temp_list)
        
#         for i in range(len(temp_list)-2):
#             if temp_list[i+1] == temp_list[i]:
#                 temp_list.remove(temp_list[i])
#         print(temp_list)
        
#         dummy_node = ListNode(-1)
        
#         if temp_list:
#             curr = ListNode(temp_list[0])
#             dummy_node.next = curr
        
#         for i in range(len(temp_list)):
#             curr.next = ListNode(temp_list[i])
#             curr = curr.next
#         return dummy_node.next

        
        