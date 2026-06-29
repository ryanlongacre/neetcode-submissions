# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create two pointers, n apart
        #when the second pointer reaches the end, then the first pointer is the node to remove
        #then remove
        original = ListNode()
        original.next = head
        first = original
        second = head
        while second and n > 0:
            second = second.next
            n -= 1
        
        while second:
            second = second.next
            first = first.next
        
        #first is the node before the one we want removed

        first.next = first.next.next


        return original.next
