



#Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # store the current node's next node as a temporory variable so that the next statement does not change the 
            # current node's next node
            temp = curr.next
            curr.next = prev
            # remember to set the pointer of the previous node to the current node before changing the pointer of the current
            # node
            prev = curr
            curr = temp
        return prev