# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #start at the ones, get a value plus a 'carry' which get added to the next
        #numbers are stored in reverse order, so the reversing part is already done for us
        #when to stop? when l1 or l2 is null
        #dd numbers together, keep track of carry. 
        #need to create the next node that will be the next thing

        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None



        return head.next


        