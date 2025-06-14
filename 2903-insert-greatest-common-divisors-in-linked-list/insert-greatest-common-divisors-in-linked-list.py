import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            n1, n2 = curr.val, curr.next.val
            curr.next = ListNode(gcd(n1,n2), curr.next)
            curr = curr.next.next
        return head

        