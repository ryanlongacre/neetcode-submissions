# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #first node in the previous group
        groupPrevious = dummy

        while True:
            kth = self.getK(groupPrevious, k)
            if not kth:
                break
            
            groupNext = kth.next #first node after the kth one (next group)
            
            prev, curr = groupNext, groupPrevious.next #prev is set to groupNext because you want the tail to point to the next group, which is what setting prev to something does
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #keep track of the original start (groupPrevious.next)
            temp = groupPrevious.next
            groupPrevious.next = kth #groupPrevious is the last element in the previous array, so its next element should be the first element in the last array, which is the last element in the old array
            groupPrevious = temp #the first element of the old array, is now the last element of the next one, so its groupPrevious
        return dummy.next #which is now the head of the list

    

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
