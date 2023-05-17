# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        idx = head_length = 0

        while curr:
            head_length += 1
            curr = curr.next
            
        mid = head_length // 2

        while head:
            if mid == idx:
                break
            head = head.next
            idx += 1
        
        return head