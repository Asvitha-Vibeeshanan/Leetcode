# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) 
        currentNew = dummy 
        currentold = head.next
        sum = 0
        while currentold is not None:
            if currentold.val == 0:
                if sum != 0:
                    currentNew.next = ListNode(sum)
                    currentNew = currentNew.next
                    sum = 0 
            else:
                sum += currentold.val
            currentold = currentold.next
        return dummy.next 