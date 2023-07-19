# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
        
#         curr = head
#         while curr.next:
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#         return head
    
    # BELOW CODE IS USING A LIST
#         temp = head
#         temp_list = []
#         while temp:
#             temp_list.append(temp.val)
#             temp = temp.next
#         print(temp_list)
        
#         i = 0
#         while i < len(temp_list)-1:
#             if temp_list[i] == temp_list[i+1]:
#                 del temp_list[i]
#             else:
#                 i = i+1
#         print(temp_list)
#         dummy_node = ListNode(-1)
        
#         if temp_list:
#             curr = ListNode(temp_list[0])
#             dummy_node.next = curr
        
#         for i in range(1, len(temp_list)):
#             curr.next = ListNode(temp_list[i])
#             curr = curr.next
#         return dummy_node.next

        
    # BELOW CODE IS USING A SET
        
        temp = head
        temp_list = []
        while temp:
            temp_list.append(temp.val)
            temp = temp.next
        print(temp_list)
        nums_set = list(set(temp_list))
        nums_set.sort()
        print(nums_set)
        dummy_node = ListNode(-1)
        
        if nums_set:
            curr = ListNode(nums_set[0])
            dummy_node.next = curr
        
        for i in range(1, len(nums_set)):
            curr.next = ListNode(nums_set[i])
            curr = curr.next
        return dummy_node.next

        
        