# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        current = head
        while(current):
            i = i + 1
            current = current.next

        if i%2 == 0:
            index = (i//2)
        else:
            index = (i//2)
        k=0
        current = head
        while(current):
            if k==index:
                print(index)
                return current
            k=k+1
            current = current.next

            
            
        
        

        