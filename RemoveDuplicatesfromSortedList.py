# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        table = {}
        table[str(head.val)] = 1
        first = head
        previous = head
        current = head.next
        while current != None:
            if str(current.val) in table:
                previous.next = current.next
            else:
                table[str(current.val)] = 1
                previous = previous.next
            current = current.next
        return first
