# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = answer = ListNode()
        while head:
            node = ListNode(val=head.val, next=curr.next)
            curr.next = node
            head = head.next
        return answer.next