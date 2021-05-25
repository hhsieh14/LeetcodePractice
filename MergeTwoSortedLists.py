# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode()
        start = head
        while l1 and l2:
            if l1.val <= l2.val:
                head.val = l1.val
                head.next = ListNode()
                l1 = l1.next
            else:
                head.val = l2.val
                head.next = ListNode()
                l2 = l2.next
            head = head.next
        # check if there is anythiong left
        if l1:
            head.val = l1.val
            head.next = l1.next
        if l2:
            head.val = l2.val
            head.next = l2.next
        return start
