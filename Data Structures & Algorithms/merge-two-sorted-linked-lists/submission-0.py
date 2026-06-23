# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        temp1 = None
        temp2 = None
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            curr = list1
            temp1 = curr.next
            temp2 = list2
        else:
            curr = list2
            temp2 = curr.next
            temp1 = list1
        
        head = curr

        while temp1 or temp2:
            if not temp1:
                while temp2:
                    curr.next = temp2
                    curr = temp2
                    temp2 = curr.next
                return head
            elif not temp2:
                while temp1:
                    curr.next = temp1
                    curr = temp1
                    temp1 = curr.next
                return head

            if temp1.val < temp2.val:
                curr.next = temp1
                curr = temp1
                temp1 = curr.next
            else:
                curr.next = temp2
                curr = temp2
                temp2 = curr.next
        return head

                
            
            
