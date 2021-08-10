# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        start = result
        carry = 0
        while(l1 != None and l2 != None):
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            result.val = digit
            if l1.next != None or l2.next != None:
                result.next = ListNode()
                result = result.next
            l1 = l1.next
            l2 = l2.next
        while(l1 != None):
            carry, digit = divmod(l1.val + carry, 10)
            result.val = digit
            if l1.next != None:
                result.next = ListNode()
                result = result.next
            l1 = l1.next
        while(l2 != None):
            carry, digit = divmod(l2.val + carry, 10)
            result.val = digit
            if l2.next != None:
                result.next = ListNode()
                result = result.next
            l2 = l2.next
        if carry != 0:
            result.next = ListNode()
            result = result.next
            result.val = carry
        return start
