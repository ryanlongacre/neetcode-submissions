# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next
        

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #when this breaks we should be at the middle of the list

        #now need to revers the second half

        prev = None
        curr = slow.next
        temp = None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #now need to alternatively add things in
        #prev is the start of the second list in reverse order
        start = head
        end = prev
        while end:
            temp = start.next
            temp2 = end.next
            start.next = end
            end.next = temp
            end = temp2
            start = temp
        



