# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        storenodesA = set()
        while pA != None:
            storenodesA.add(pA)
            pA = pA.next
            
        while pB != None:
            if pB in storenodesA:
                return pB
            else:
                pB = pB.next
        return None
####set look up is only O(1)#####
####Time:O(N+M);Space:O(N)#####
